from uuid import uuid4
import json,html
from shared.settings import settings
def write_report(result,formats):
    rid=uuid4().hex;root=settings.data_root/"greengeck0"/"reports"/rid;root.mkdir(parents=True,exist_ok=True);outputs={}
    if "json" in formats or "raw" in formats:
        p=root/"report.json";p.write_text(json.dumps(result,indent=2,default=str));outputs["json"]=str(p)
    if "html" in formats or "pdf" in formats:
        p=root/"report.html";p.write_text(f"<html><body><h1>Green Geck0 Report</h1><pre>{html.escape(json.dumps(result,indent=2,default=str))}</pre></body></html>");outputs["html"]=str(p)
    if "pdf" in formats:
        try:
            from reportlab.pdfgen import canvas
            p=root/"report.pdf";c=canvas.Canvas(str(p));c.drawString(40,800,"Green Geck0 Report");y=780
            for line in json.dumps(result,indent=2,default=str).splitlines()[:55]:c.drawString(40,y,line[:100]);y-=13
            c.save();outputs["pdf"]=str(p)
        except Exception:outputs["pdf"]="unavailable"
    return rid,outputs
