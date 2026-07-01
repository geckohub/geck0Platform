#!/usr/bin/env python3
import os, socket, subprocess, psutil, random
from datetime import datetime
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static, Input, Footer

HOME = os.path.expanduser("~/geck0Platform")

GECKOS = [
r"""
        __..------..__                      __..------..__
    _.-'   0    0    '-._              _.-'    0   0     '-._
  .'        .____.        '.__________.'         .____.        '.
 /       G E C K 0          COMMAND CENTRE          G E C K 0    \
 '.___              ___________________              _________.'
      '------------'                   '------------'
""",
r"""
      /\        /\________________________________________________/\        /\
     /  \  0 0 /        G E C K 0   C O M M A N D   C E N T R E   \ 0 0   /  \
    /____\____/          CONTROL • AUTOMATE • PROTECT • EXPLORE    \____/____\
          \___        _______________________________________       ___/
              \______/
""",
r"""
        ____                 ____                 ____
      .'    '._____________.'    '._____________.'    '.
     /  0  0  \           /  0  0  \           /  0  0  \
    |    __    |  G E C K 0   C O M M A N D   C E N T R E |
     \  \__/  /___________\  \__/  /___________\  \__/  /
      '.___.'               '.___.'               '.___.'
""",
]
SELECTED = random.choice(GECKOS)

THEMES = ["matrix", "amber", "ice", "red", "kali", "toxic"]
COLORS = {
    "matrix": ("#39ff14", "#00ff66", "#010601"),
    "amber": ("#ffbf00", "#ff9900", "#080500"),
    "ice": ("#00e5ff", "#00aaff", "#00070a"),
    "red": ("#ff3333", "#ff5555", "#090000"),
    "kali": ("#00b7ff", "#0077ff", "#01030a"),
    "toxic": ("#ccff00", "#aaff00", "#050800"),
}

def sh(cmd, timeout=2):
    try:
        return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.DEVNULL, timeout=timeout).strip()
    except Exception:
        return "n/a"

def svc(name):
    return "● ONLINE" if sh(f"systemctl is-active {name}") == "active" else "○ OFFLINE"

def blink(art):
    return art.replace("0  0", "-  -").replace("0   0", "-   -").replace("0 0", "- -")

def bar(p, w=18):
    f = int((float(p) / 100) * w)
    return "█" * f + "░" * (w - f)

def firehose():
    return sh("cd /home/lucy/geckoscan1.0 2>/dev/null && latest=$(find logs v9/output -type f -name '*.log' 2>/dev/null | xargs -r ls -t | head -1); [ -n \"$latest\" ] && echo $latest && tail -n 6 \"$latest\"", 3)

class Geck0Centre(App):
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("x", "quit", "Exit"),
        ("r", "refresh_panels", "Refresh"),
        ("s", "focus_cmd", "Command"),
        ("f5", "cycle_theme", "Theme"),
    ]

    CSS = """
    Screen { background: #010601; color: #39ff14; }
    #banner { border: heavy #00ff66; color: #39ff14; height: 12; text-align: center; padding: 0 1; }
    .panel { border: round #00ff66; color: #39ff14; padding: 1; margin: 1; height: 34; }
    #left { width: 22%; }
    #middle { width: 56%; }
    #right { width: 22%; }
    #cmd { border: heavy #00ff66; color: #39ff14; background: #010601; margin: 0 1 1 1; }
    """

    theme_idx = 0
    blink_on = False

    def compose(self) -> ComposeResult:
        yield Static("", id="banner")
        with Horizontal():
            yield Static("", id="left", classes="panel")
            yield Static("", id="middle", classes="panel")
            yield Static("", id="right", classes="panel")
        yield Input(placeholder="Geck0> search ketama | scan mmcy.uk | report latest | crumble | cyberx | git status | theme matrix", id="cmd")
        yield Footer()

    def on_mount(self):
        self.set_interval(0.8, self.animate)
        self.set_interval(2, self.refresh_panels)
        self.refresh_panels()
        self.query_one("#cmd", Input).focus()

    def animate(self):
        self.blink_on = not self.blink_on
        art = blink(SELECTED) if self.blink_on else SELECTED
        self.query_one("#banner", Static).update(
            art + f"\n🦎 CONTROL • AUTOMATE • PROTECT • EXPLORE     THEME: {THEMES[self.theme_idx].upper()}     F5 SWITCH"
        )

    def refresh_panels(self):
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent
        temp = sh("cat /sys/class/thermal/thermal_zone0/temp 2>/dev/null")
        temp = f"{int(temp)/1000:.1f}°C" if temp.isdigit() else "n/a"
        scans = sh("tmux ls 2>/dev/null | grep -c geck0scan || true")
        docker = sh("docker ps --format '{{.Names}}' 2>/dev/null | wc -l")

        self.query_one("#left", Static).update(f"""
🖥 SYSTEM STATUS

HOST       {socket.gethostname()}
USER       lucy
ROOT       {HOME}
IP         {sh("hostname -I | awk '{print $1}'")}
TAILSCALE  {sh("tailscale ip -4 2>/dev/null")}

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

        self.query_one("#middle", Static).update(f"""
« MAIN CONTROL MENU »

  1  🛡  BlackGeck0       Recon • GeckoScan • GeckoExploit • Geck0Report
  2  🧪 GreenGeck0       Automated tests • QA • Evidence • Client reports
  3  💗 PinkGeck0        Digital products • Sites • Apps • BreadCrumbs
  4  🎨 BlueGeck0        Design • Images • Print media • Spreadshirt
  5  🟡 YellowGeck0      RobotRainforest • Storefronts • Commerce
  6  🟣 PurpleGeck0      Discord • Telegram • WhatsApp • Mail webhooks

  7  🗣  Crumble          Voice • Chat • Commands • Mirror
  8  🧠 CyberX           AI router • ChatGPT • Claude • Gemini • Ollama
  9  🔎 Geck0 Search     Notes • Files • Photos • Voice • Wiki • Git
 10  📄 Geck0Report      Client PDFs • SaaS reports • Evidence packs
 11  🕸  Knowledge Graph  Entities • Links • Memory • Timelines
 12  📊 Dashboard        Clean view • Full control centre
 13  📚 Wiki             Architecture • Roadmaps • Playbooks
 14  🧬 Git              Status • Commit • Push • Sync

🔥 MINI FIREHOSE

Running scans: {scans}

{firehose()[:500]}
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

🎨 THEMES

{", ".join(THEMES)}

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
        self.theme_idx = (self.theme_idx + 1) % len(THEMES)
        self.refresh_panels()

    def on_input_submitted(self, event: Input.Submitted):
        cmd = event.value.strip()
        event.input.value = ""
        if cmd in ("x", "q", "exit", "quit"):
            self.exit()
        elif cmd.startswith("theme "):
            wanted = cmd.split(" ", 1)[1].strip()
            if wanted in THEMES:
                self.theme_idx = THEMES.index(wanted)
                self.refresh_panels()
        else:
            self.query_one("#right", Static).update(f"COMMAND OUTPUT\n\n{cmd}\n\nFuture: route through Geck0 command engine.")

if __name__ == "__main__":
    Geck0Centre().run()
