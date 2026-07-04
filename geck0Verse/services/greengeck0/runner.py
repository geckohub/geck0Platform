from urllib.parse import urlparse
import ssl,socket,httpx,ipaddress,os
SAFE_TESTS={"http","headers","tls","html","robots"}

def guard_host(hostname):
    if os.getenv("GREEN_ALLOW_PRIVATE","false").lower()=="true": return
    addresses={item[4][0] for item in socket.getaddrinfo(hostname,None)}
    for raw in addresses:
        ip=ipaddress.ip_address(raw)
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or ip.is_multicast:
            raise ValueError("Private/reserved targets are blocked by default; set GREEN_ALLOW_PRIVATE=true only for authorised lab testing")
async def run_checks(url,tests):
    parsed=urlparse(url)
    if parsed.scheme not in {"http","https"} or not parsed.hostname:raise ValueError("A valid http(s) URL is required")
    guard_host(parsed.hostname)
    selected=[t for t in tests if t in SAFE_TESTS] or ["http","headers"];result={"url":url,"tests":selected,"findings":[]}
    async with httpx.AsyncClient(timeout=15,follow_redirects=True,headers={"User-Agent":"GreenGeck0/2.0 defensive-check"}) as client:
        r=await client.get(url);result["status_code"]=r.status_code;result["final_url"]=str(r.url);result["headers"]=dict(r.headers)
        if "headers" in selected:
            for h in ["content-security-policy","strict-transport-security","x-content-type-options","referrer-policy"]:
                if h not in r.headers:result["findings"].append({"severity":"info","check":h,"message":"Recommended response header not observed"})
        if "html" in selected:result["html_summary"]={"bytes":len(r.content),"has_title":"<title" in r.text.lower(),"has_viewport":"viewport" in r.text.lower()}
        if "robots" in selected:result["robots_status"]=(await client.get(f"{parsed.scheme}://{parsed.netloc}/robots.txt")).status_code
    if "tls" in selected and parsed.scheme=="https":
        ctx=ssl.create_default_context()
        with socket.create_connection((parsed.hostname,parsed.port or 443),timeout=8) as sock:
            with ctx.wrap_socket(sock,server_hostname=parsed.hostname) as ssock:
                cert=ssock.getpeercert();result["tls"]={"version":ssock.version(),"expires":cert.get("notAfter"),"issuer":cert.get("issuer")}
    return result
