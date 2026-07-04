package uk.geckohub.crumble

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.provider.OpenableColumns
import android.speech.RecognizerIntent
import android.speech.tts.TextToSpeech
import android.webkit.WebView
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import androidx.compose.ui.viewinterop.AndroidView
import kotlinx.coroutines.launch
import okhttp3.MediaType.Companion.toMediaTypeOrNull
import okhttp3.MultipartBody
import okhttp3.RequestBody.Companion.toRequestBody
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import java.util.Locale

class MainActivity : ComponentActivity(), TextToSpeech.OnInitListener {
    private lateinit var tts: TextToSpeech
    private var speechCallback: ((String) -> Unit)? = null
    private var fileCallback: ((Uri) -> Unit)? = null

    private val speech = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result ->
        val text = result.data?.getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS)?.firstOrNull()
        if (text != null) speechCallback?.invoke(text)
    }
    private val filePicker = registerForActivityResult(ActivityResultContracts.GetContent()) { uri ->
        if (uri != null) fileCallback?.invoke(uri)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        tts = TextToSpeech(this, this)
        setContent {
            CrumbleApp(
                listen = { cb ->
                    speechCallback = cb
                    speech.launch(Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH).apply {
                        putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM)
                        putExtra(RecognizerIntent.EXTRA_LANGUAGE, "en-GB")
                    })
                },
                speak = { tts.speak(it, TextToSpeech.QUEUE_FLUSH, null, "crumble") },
                pickFile = { cb -> fileCallback = cb; filePicker.launch("*/*") },
                readFile = { uri ->
                    var name = "upload.bin"
                    contentResolver.query(uri, null, null, null, null)?.use { cursor ->
                        val index = cursor.getColumnIndex(OpenableColumns.DISPLAY_NAME)
                        if (index >= 0 && cursor.moveToFirst()) name = cursor.getString(index)
                    }
                    name to (contentResolver.openInputStream(uri)?.use { it.readBytes() } ?: ByteArray(0))
                }
            )
        }
    }

    override fun onInit(status: Int) {
        if (status == TextToSpeech.SUCCESS) tts.language = Locale.UK
    }
}

@Composable
fun CrumbleApp(
    listen: (((String) -> Unit) -> Unit),
    speak: (String) -> Unit,
    pickFile: (((Uri) -> Unit) -> Unit),
    readFile: (Uri) -> Pair<String, ByteArray>
) {
    val context = LocalContext.current
    val prefs = remember { context.getSharedPreferences("crumble", 0) }
    var base by remember { mutableStateOf(prefs.getString("base", "http://192.168.1.244:8080/")!!) }
    var token by remember { mutableStateOf(prefs.getString("token", "")!!) }
    var message by remember { mutableStateOf("") }
    var output by remember { mutableStateOf("Ready") }
    var tab by remember { mutableIntStateOf(0) }
    var domains by remember { mutableStateOf(emptyList<Domain>()) }
    var webUrl by remember { mutableStateOf(base.replace(":8080/", ":8088/")) }
    val scope = rememberCoroutineScope()

    fun api(): CrumbleApi = Retrofit.Builder()
        .baseUrl(base)
        .addConverterFactory(GsonConverterFactory.create())
        .build()
        .create(CrumbleApi::class.java)

    MaterialTheme {
        Scaffold(
            topBar = { TopAppBar(title = { Text("Crumble") }) },
            bottomBar = {
                NavigationBar {
                    val labels = listOf("Chat", "Domains", "Upload", "Web", "Settings")
                    val icons = listOf("💬", "🦎", "⬆", "🗺", "⚙")
                    labels.forEachIndexed { i, label ->
                        NavigationBarItem(selected = tab == i, onClick = { tab = i }, icon = { Text(icons[i]) }, label = { Text(label) })
                    }
                }
            }
        ) { padding ->
            Column(Modifier.padding(padding).padding(16.dp).fillMaxSize()) {
                when (tab) {
                    0 -> {
                        OutlinedTextField(message, { message = it }, label = { Text("Ask Crumble") }, modifier = Modifier.fillMaxWidth())
                        Row {
                            Button(onClick = { listen { message = it } }) { Text("Voice") }
                            Spacer(Modifier.width(8.dp))
                            Button(onClick = {
                                scope.launch {
                                    try {
                                        val response = api().chat(token, ChatRequest(message))
                                        output = response.answer
                                        speak(response.answer)
                                    } catch (e: Exception) { output = e.message ?: "Error" }
                                }
                            }) { Text("Send") }
                        }
                        Text(output, Modifier.padding(top = 16.dp))
                    }
                    1 -> {
                        Button(onClick = {
                            scope.launch {
                                try { domains = api().domains(token).domains; output = "Loaded ${domains.size} domains" }
                                catch (e: Exception) { output = e.message ?: "Error" }
                            }
                        }) { Text("Refresh domains") }
                        LazyColumn {
                            items(domains) { domain ->
                                Card(Modifier.fillMaxWidth().padding(vertical = 4.dp)) {
                                    Column(Modifier.padding(12.dp)) {
                                        Text(domain.id, style = MaterialTheme.typography.titleMedium)
                                        Text("${domain.family} • ${domain.host} • ${domain.status}")
                                        domain.dashboard?.let { url ->
                                            Button(onClick = { webUrl = url; tab = 3 }) { Text("Open dashboard") }
                                        }
                                    }
                                }
                            }
                        }
                    }
                    2 -> {
                        Text("Upload images, requirements, documents or other project inputs to Crumble.")
                        Button(onClick = {
                            pickFile { uri ->
                                scope.launch {
                                    try {
                                        val (name, bytes) = readFile(uri)
                                        val body = bytes.toRequestBody("application/octet-stream".toMediaTypeOrNull())
                                        val part = MultipartBody.Part.createFormData("file", name, body)
                                        output = api().upload(token, part).toString()
                                    } catch (e: Exception) { output = e.message ?: "Upload failed" }
                                }
                            }
                        }) { Text("Choose and upload file") }
                        Text(output, Modifier.padding(top = 16.dp))
                    }
                    3 -> {
                        Text(webUrl, style = MaterialTheme.typography.bodySmall)
                        AndroidView(
                            modifier = Modifier.fillMaxSize(),
                            factory = { WebView(it).apply { settings.javaScriptEnabled = true; loadUrl(webUrl) } },
                            update = { if (it.url != webUrl) it.loadUrl(webUrl) }
                        )
                    }
                    4 -> {
                        OutlinedTextField(base, { base = it }, label = { Text("JE Hub URL") }, modifier = Modifier.fillMaxWidth())
                        OutlinedTextField(token, { token = it }, label = { Text("API token") }, modifier = Modifier.fillMaxWidth())
                        Button(onClick = {
                            prefs.edit().putString("base", base).putString("token", token).apply()
                            webUrl = base.replace(":8080/", ":8088/")
                            output = "Settings saved"
                        }) { Text("Save") }
                        Text(output)
                    }
                }
            }
        }
    }
}
