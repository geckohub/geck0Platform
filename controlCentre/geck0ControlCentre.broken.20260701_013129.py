#!/usr/bin/env python3
import os, socket, subprocess, psutil, random
from datetime import datetime
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static, Input, Footer, Button

HOME = os.path.expanduser("~/geck0Platform")

THEMES = {
    "matrix":  {"fg": "#39ff14", "border": "#00ff66", "bg": "#010601"},
    "amber":   {"fg": "#ffbf00", "border": "#ff9900", "bg": "#080500"},
    "ice":     {"fg": "#00e5ff", "border": "#00aaff", "bg": "#00070a"},
    "red":     {"fg": "#ff3333", "border": "#ff5555", "bg": "#090000"},
    "kali":    {"fg": "#00b7ff", "border": "#0077ff", "bg": "#01030a"},
    "purple":  {"fg": "#c77dff", "border": "#9d4edd", "bg": "#050008"},
    "ghost":   {"fg": "#d8f3dc", "border": "#95d5b2", "bg": "#020402"},
    "toxic":   {"fg": "#ccff00", "border": "#aaff00", "bg": "#050800"},
}

GECKOS = [
r"""
        ____                 ____                 ____
      .'    '._____________.'    '._____________.'    '.
     /  0  0  \           /  0  0  \           /  0  0  \
    |    __    |  G E C K 0   C O M M A N D   C E N T R E |
     \  \__/  /___________\  \__/  /___________\  \__/  /
      '.___.'               '.___.'               '.___.'
           \_____       _________       _________/
                 \_____/         \_____/
""",
r"""
      /\        /\________________________________________________/\        /\
     /  \  0 0 /                                                  \ 0 0   /  \
    /____\____/       G E C K 0   C O M M A N D   C E N T R E      \____/____\
          \___        CONTROL • AUTOMATE • PROTECT • EXPLORE       ___/
              \__________________________________________________/
""",
r"""
        __..------..__                      __..------..__
    _.-'   0    0    '-._              _.-'    0   0     '-._
  .'        .____.        '.__________.'         .____.        '.
 /       G E C K 0          COMMAND CENTRE          G E C K 0    \
 '.___              ___________________              _________.'
      '------------'                   '------------'
""",
]

SELECTED_GECKO = random.choice(GECKOS)

def blink(art: str) -> str:
    return art.replace("0  0", "-  -").replace("0   0", "-   -").replace("0 0", "- -")

def sh(cmd, timeout=2):
    try:
        return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.DEVNULL, timeout=timeout).strip()
    except Exception:
        return "n/a"

def svc(name):
    return "● ONLINE" if sh(f"systemctl is-active {name}") == "active" else "○ OFFLINE"

def bar(p, w=18):
    f = int((float(p) / 100) * w)
    return "█" * f + "░" * (w - f)

def latest_scan_firehose():
    cmd = r"""
    cd /home/lucy/geckoscan1.0 2>/dev/null || exit 0
    latest=$(find logs v9/output -type f \( -name "*.log" -o -name "*.txt" \) 2>/dev/null | xargs -r ls -t 2>/dev/null | head -1)
    [ -n "$latest" ] && echo "FILE: $latest" && tail -n 8 "$latest"
    """
    return sh(cmd, timeout=3)

class Geck0Centre(App):
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("x", "quit", "Exit"),
        ("r", "refresh_panels", "Refresh"),
        ("s", "focus_cmd", "Command"),
        ("f5", "cycle_theme", "Theme"),
    ]

    theme_name = "matrix"
    blink_on = False

    def compose(self) -> ComposeResult:
        yield Static("", id="banner")
        with Horizontal():
            yield Static("", id="left", classes="panel")
            with Vertical(id="middle", classes="panel"):
                yield Static("« MAIN CONTROL MENU »", id="menuTitle")
                for label in [
                    "🛡 BlackGeck0", "🧪 GreenGeck0", "💗 PinkGeck0", "🎨 BlueGeck0",
                    "🟡 YellowGeck0", "🟣 PurpleGeck0", "🗣 Crumble", "🧠 CyberX",
                    "🔎 Geck0 Search", "📄 Geck0Report", "🕸 Knowledge Graph",
                    "📊 Dashboard", "📚 Wiki", "🧬 Git"
                ]:
                    yield Button(label, id=label.split(" ", 1)[1].replace(" ", "_").lower())
                yield Static("", id="firehose")
            yield Static("", id="right", classes="panel")
        yield Input(placeholder="Geck0> search ketama | scan mmcy.uk | report latest | crumble | cyberx | git status | theme matrix", id="cmd")
        yield Footer()

    def on_mount(self):
        self.apply_theme()
        self.set_interval(0.7, self.animate_banner)
        self.set_interval(2, self.refresh_panels)
        self.refresh_panels()
        self.query_one("#cmd", Input).focus()

    def apply_theme(self):
        t = THEMES[self.theme_name]
        self.styles.background = t["bg"]
        css = f"""
        #banner {{
            color: {t["fg"]};
            border: heavy {t["border"]};
            padding: 0 1;
            text-align: center;
            height: 12;
        }}
        .panel {{
            border: round {t["border"]};
            color: {t["fg"]};
            padding: 1;
            margin: 1;
            height: 36;
        }}
        #left {{ width: 22%; }}
        #middle {{ width: 56%; }}
        #right {{ width: 22%; }}
        Button {{
            color: {t["fg"]};
            border: none;
            background: {t["bg"]};
            min-height: 1;
            height: 1;
        }}
        Button:hover {{
            background: {t["border"]};
            color: black;
        }}
        #firehose {{
            margin-top: 1;
            border-top: solid {t["border"]};
            height: 10;
        }}
        #cmd {{
            color: {t["fg"]};
            border: heavy {t["border"]};
            background: {t["bg"]};
            margin: 0 1 1 1;
        }}
        """
                self.stylesheet.add_source(css)
        self.refresh_css()

    def animate_banner(self):
        self.blink_on = not self.blink_on
        art = blink(SELECTED_GECKO) if self.blink_on else SELECTED_GECKO
        self.query_one("#banner", Static).update(
            art + f"\n🦎 CONTROL • AUTOMATE • PROTECT • EXPLORE     THEME: {self.theme_name.upper()}     F5 SWITCH"
        )

    def refresh_panels(self):
        host = socket.gethostname()
        ip = sh("hostname -I | awk '{print $1}'")
        ts = sh("tailscale ip -4 2>/dev/null")
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent
        docker = sh("docker ps --format '{{.Names}}' 2>/dev/null | wc -l")
        scans = sh("tmux ls 2>/dev/null | grep -c geck0scan || true")
        git_changes = sh(f"git -C {HOME} status --short 2>/dev/null | wc -l")
        temp = sh("cat /sys/class/thermal/thermal_zone0/temp 2>/dev/null")
        temp = f"{int(temp)/1000:.1f}°C" if temp.isdigit() else "n/a"

        self.query_one("#left", Static).update(f"""
🖥 SYSTEM STATUS

HOST       {host}
USER       lucy
ROOT       {HOME}
IP         {ip}
TAILSCALE  {"● ONLINE " + ts if ts.startswith("100.") else "○ CHECK"}

UPTIME     {sh("uptime -p")}
TEMP       {temp}

CPU        [{bar(cpu)}] {cpu:.0f}%
MEMORY     [{bar(mem)}] {mem:.0f}%
DISK       [{bar(disk)}] {disk:.0f}%

⚙ SERVICES

Docker     {docker} containers
SSH        {svc("ssh")}
Fail2ban   {svc("fail2ban")}
Grafana    {svc("grafana-server")}
Nginx      {svc("nginx")}
Mosquitto  {svc("mosquitto")}
""")

        self.query_one("#firehose", Static).update(f"""
🔥 MINI FIREHOSE

Running scans: {scans}

{latest_scan_firehose()[:650]}
""")

        self.query_one("#right", Static).update(f"""
🦎 GECK0 STATUS

MODE           COMMAND
TIME           {datetime.now().strftime("%H:%M:%S")}
CYBERX         ● READY
CRUMBLE        ● READY
SEARCH         ◐ BOOTSTRAP
GRAPH          ○ PLANNED

🛡 BLACKGECK0

Running scans  {scans}
GeckoScan      ThaiGreen
GeckoAir       ThaiGreen
GeckoStealth   ThaiGreen
GeckoExploit   Premium/SaaS
Geck0Report    Client product

🧬 DEV STATUS

Git changes    {git_changes}

🎨 THEMES

matrix amber ice red
kali purple ghost toxic

COMMANDS

theme matrix
search ketama
scan mmcy.uk
report latest
crumble
cyberx
git status
""")

    def action_focus_cmd(self):
        self.query_one("#cmd", Input).focus()

    def action_refresh_panels(self):
        self.refresh_panels()

    def action_cycle_theme(self):
        names = list(THEMES)
        self.theme_name = names[(names.index(self.theme_name) + 1) % len(names)]
        self.apply_theme()
        self.refresh_panels()

    def on_button_pressed(self, event: Button.Pressed):
        self.query_one("#right", Static).update(f"""
CLICKED MENU ITEM

{event.button.label}

Future: open module screen.

Tip:
Use command bar for now.
""")

    def on_input_submitted(self, event: Input.Submitted):
        cmd = event.value.strip()
        event.input.value = ""

        if cmd in ("x", "q", "exit", "quit"):
            self.exit()
            return
        if cmd.startswith("theme "):
            wanted = cmd.split(" ", 1)[1].strip()
            if wanted in THEMES:
                self.theme_name = wanted
                self.apply_theme()
                self.refresh_panels()
                return
            out = f"Unknown theme: {wanted}. Available: {', '.join(THEMES)}"
        elif cmd.startswith("git"):
            out = sh(f"git -C {HOME} {cmd[4:] or 'status'}", timeout=4)
        elif cmd.startswith("scan"):
            out = f"Future: send GeckoScan request to ThaiGreen → {cmd}"
        elif cmd.startswith("search"):
            out = f"Future: Geck0 Search query → {cmd[7:]}"
        elif cmd.startswith("report"):
            out = f"Future: Geck0Report workflow → {cmd}"
        else:
            out = f"Command received: {cmd}"

        self.query_one("#right", Static).update(f"""
COMMAND OUTPUT

{out}
""")

if __name__ == "__main__":
    Geck0Centre().run()
