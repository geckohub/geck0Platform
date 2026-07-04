#!/usr/bin/env python3
import argparse,json,os,urllib.request
DEFAULT_BASE=os.getenv("CRUMBLE_URL","http://192.168.1.244:8080").rstrip("/")
DEFAULT_TOKEN=os.getenv("GECK0_API_TOKEN","")
def request(base,token,path,method="GET",payload=None):
    data=None if payload is None else json.dumps(payload).encode()
    req=urllib.request.Request(base+path,data=data,method=method,headers={"X-Geck0-Token":token,"Content-Type":"application/json"})
    with urllib.request.urlopen(req,timeout=60) as response:return json.load(response)
def main():
    parser=argparse.ArgumentParser();parser.add_argument("--url",default=DEFAULT_BASE);parser.add_argument("--token",default=DEFAULT_TOKEN);sub=parser.add_subparsers(dest="cmd",required=True)
    chat=sub.add_parser("chat");chat.add_argument("message",nargs="+");sub.add_parser("domains");sub.add_parser("suggestions");history=sub.add_parser("history");history.add_argument("--limit",type=int,default=20)
    args=parser.parse_args();base=args.url.rstrip("/");token=args.token
    if args.cmd=="chat":output=request(base,token,"/v1/chat","POST",{"message":" ".join(args.message)})
    elif args.cmd=="domains":output=request(base,token,"/v1/domains")
    elif args.cmd=="suggestions":output=request(base,token,"/v1/suggestions")
    else:output=request(base,token,f"/v1/history?limit={args.limit}")
    print(json.dumps(output,indent=2))
if __name__=="__main__":main()
