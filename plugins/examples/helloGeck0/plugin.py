from geck0 import Geck0Plugin

class HelloGeck0(Geck0Plugin):
    name = "Hello Geck0"
    version = "0.1.0"
    category = "example"
    commands = ["hello"]

    def run(self, command, args=""):
        return f"🦎 Hello from Geck0 SDK. Args={args}"
