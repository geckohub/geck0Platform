import os
from fastapi.middleware.cors import CORSMiddleware

def configure_web(app):
    raw=os.getenv("GECK0_CORS_ORIGINS","*")
    origins=[x.strip() for x in raw.split(",") if x.strip()] or ["*"]
    app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=False,allow_methods=["GET","POST","PUT","PATCH","DELETE","OPTIONS"],allow_headers=["*"])
    return app
