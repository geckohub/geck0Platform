package uk.geckohub.crumble
import okhttp3.MultipartBody
import retrofit2.http.*
data class ChatRequest(val message:String)
data class ChatResponse(val answer:String,val intent:Map<String,Any>?,val data:Any?)
data class Domain(val id:String,val family:String,val host:String,val status:String,val dashboard:String?)
data class DomainsResponse(val domains:List<Domain>)
interface CrumbleApi {
 @POST("v1/chat") suspend fun chat(@Header("X-Geck0-Token") token:String,@Body req:ChatRequest):ChatResponse
 @GET("v1/domains") suspend fun domains(@Header("X-Geck0-Token") token:String):DomainsResponse
 @Multipart @POST("v1/uploads") suspend fun upload(@Header("X-Geck0-Token") token:String,@Part file:MultipartBody.Part):Map<String,Any>
}
