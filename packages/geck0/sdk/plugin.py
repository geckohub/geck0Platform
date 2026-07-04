class Geck0Plugin:
    name = "UnnamedPlugin"
    version = "0.1.0"
    category = "shared"
    commands = []
    widgets = []
    permissions = []

    def status(self):
        return {
            "name": self.name,
            "version": self.version,
            "category": self.category,
            "commands": self.commands,
            "widgets": self.widgets,
            "permissions": self.permissions,
        }

    def run(self, command: str, args: str = ""):
        return f"{self.name} received command={command} args={args}"
