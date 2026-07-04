from pathlib import Path
import os,shutil,subprocess,smtplib
from email.message import EmailMessage
import httpx

EXPORT_ROOT=Path(os.getenv("GREEN_EXPORT_ROOT","/workspace/geck0Projects/greenGeck0/exports"))
async def deliver(result,outputs,delivery):
    status={}
    webhook=delivery.get("webhook_url")
    if webhook:
        try:
            async with httpx.AsyncClient(timeout=20) as client:
                r=await client.post(webhook,json={"result":result,"outputs":outputs});r.raise_for_status();status["webhook"]="sent"
        except Exception as exc:status["webhook"]=f"failed: {exc}"
    email_to=delivery.get("email_to")
    if email_to:
        try:
            host=os.getenv("SMTP_HOST","");port=int(os.getenv("SMTP_PORT","587"));user=os.getenv("SMTP_USERNAME","");password=os.getenv("SMTP_PASSWORD","")
            if not host:raise RuntimeError("SMTP_HOST is not configured")
            msg=EmailMessage();msg["Subject"]="Green Geck0 test report";msg["From"]=os.getenv("SMTP_FROM",user or "greengeck0@local");msg["To"]=email_to;msg.set_content(str(result))
            with smtplib.SMTP(host,port,timeout=20) as smtp:
                smtp.starttls()
                if user:smtp.login(user,password)
                smtp.send_message(msg)
            status["email"]="sent"
        except Exception as exc:status["email"]=f"failed: {exc}"
    repo_name=delivery.get("git_repo")
    if repo_name:
        safe="".join(c for c in repo_name if c.isalnum() or c in "-_" )[:64]
        try:
            if not safe:raise ValueError("Invalid git_repo")
            target=(EXPORT_ROOT/safe).resolve();root=EXPORT_ROOT.resolve()
            if root not in target.parents:raise ValueError("Unsafe git path")
            target.mkdir(parents=True,exist_ok=True)
            for name,path in outputs.items():
                src=Path(path)
                if src.exists():shutil.copy2(src,target/src.name)
            subprocess.run(["git","init","-b","main"],cwd=target,check=False,capture_output=True);subprocess.run(["git","add","."],cwd=target,check=True);subprocess.run(["git","-c","user.name=Green Geck0","-c","user.email=green@local","commit","-m","Add test report"],cwd=target,check=False,capture_output=True)
            status["git"]={"repo":str(target)}
        except Exception as exc:status["git"]=f"failed: {exc}"
    return status
