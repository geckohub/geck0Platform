plugins { id("com.android.application"); id("org.jetbrains.kotlin.android"); id("org.jetbrains.kotlin.plugin.compose") }
android {
    namespace = "uk.geckohub.crumble"; compileSdk = 37
    defaultConfig { applicationId = "uk.geckohub.crumble"; minSdk = 26; targetSdk = 36; versionCode = 1; versionName = "2.0.0" }
    buildFeatures { compose = true; buildConfig = true }
    buildTypes { release { isMinifyEnabled = false; proguardFiles(getDefaultProguardFile("proguard-android-optimize.txt"), "proguard-rules.pro") } }
    compileOptions { sourceCompatibility = JavaVersion.VERSION_17; targetCompatibility = JavaVersion.VERSION_17 }
    kotlinOptions { jvmTarget = "17" }
}
dependencies {
    val composeBom = platform("androidx.compose:compose-bom:2026.06.00")
    implementation(composeBom); androidTestImplementation(composeBom)
    implementation("androidx.activity:activity-compose:1.13.0"); implementation("androidx.compose.material3:material3"); implementation("androidx.compose.ui:ui"); implementation("androidx.compose.ui:ui-tooling-preview"); debugImplementation("androidx.compose.ui:ui-tooling")
    implementation("androidx.lifecycle:lifecycle-runtime-compose:2.10.0"); implementation("androidx.navigation:navigation-compose:2.9.0")
    implementation("com.squareup.retrofit2:retrofit:2.11.0"); implementation("com.squareup.retrofit2:converter-gson:2.11.0"); implementation("com.squareup.okhttp3:logging-interceptor:4.12.0"); implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.10.2")
}
