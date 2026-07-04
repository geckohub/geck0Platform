import random
from datetime import datetime
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static, Input, Footer, Button

from .themes import THEMES
from .geckos import choose_gecko, blink
from .stats import system_panel
from .scans import scan_counts, latest_scan_log, active_scan_processes
from .router import route

MENU_ITEMS = [
    ("01", "🛡", "BlackGeck0", "Recon • GeckoScan • GeckoExploit • Geck0Report"),
    ("02", "🧪", "GreenGeck0", "Automated tests • QA • Evidence • Reports"),
    ("03", "💗", "PinkGeck0", "Digital products • Sites • Apps • BreadCrumbs"),
    ("04", "🎨", "BlueGeck0", "Design • Images • Print media • Spreadshirt"),
    ("05", "🟡", "YellowGeck0", "RobotRainforest • Storefronts • Commerce"),
    ("06", "🟣", "PurpleGeck0", "Discord • Telegram • WhatsApp • Webhooks"),
    ("07", "🗣", "Crumble", "Voice • Chat • Commands • Mirror"),
    ("08", "🧠", "CyberX", "AI router • ChatGPT • Claude • Gemini • Ollama"),
    ("09", "🔎", "Geck0 Search", "Notes • Files • Photos • Voice • Wiki • Git"),
    ("10", "📄", "Geck0Report", "Client PDFs • SaaS reports • Evidence packs"),
    ("11", "🕸", "Knowledge Graph", "Entities • Links • Memory • Timelines"),
    ("12", "📊", "Dashboard", "Clean view • Full control centre"),
    ("13", "📚", "Wiki", "Architecture • Roadmaps • Playbooks"),
    ("14", "🧬", "Git", "Status • Commit • Push • Sync"),
]

class Geck0LiveApp(App):
    CSS = """
    Screen { background: #010601; color: #39ff14; }
    #banner { height: 11; text-align: center; padding: 0 1; }
    .panel { padding: 1; margin: 1; height: 38; }
    #left { width: 24%; }
    #middle { width: 52%; }
    #right { width: 24%; }
    Button { height: 1; min-height: 1; border: none; text-align: left; }
    #firehose { height: 12; margin-top: 1; }
    #cmd { margin: 0 1 1 1; }
    """
    BINDINGS = [
        ("q", "quit", "Quit"), ("x", "quit", "Exit"),
        ("r", "refresh_panels", "Refresh"), ("s", "focus_cmd", "Command"),
        ("f5", "cycle_theme", "Theme"),
    ]

    def __init__(self):
        super().__init__()
        self.theme_names = list(THEMES)
        self.theme_idx = 0
        self.blink_on = False
        self.gecko = choose_gecko()

    def compose(self) -> ComposeResult:
        yield Static("", id="banner")
        with Horizontal():
            yield Static("", id="left", classes="panel")
            with Vertical(id="middle", classes="panel"):
                yield Static("", id="menuTitle")
                for n, icon, name, desc in MENU_ITEMS:
                    yield Button(f"{n}  {icon}  {name:<16} {desc}", id=f"menu_{n}")
                yield Static("", id="firehose")
            yield Static("", id="right", classes="panel")
        yield Input(placeholder="Geck0> scan trex mmcy.uk | show latest scan results | firehose | running scans | search ketama | theme matrix", id="cmd")
        yield Footer()

    def on_mount(self):
        self.apply_theme()
        self.set_interval(0.8, self.animate)
        self.set_interval(2, self.refresh_panels)
        self.refresh_panels()
        self.query_one("#cmd", Input).focus()

    def colours(self):
        return THEMES[self.theme_names[self.theme_idx]]

    def apply_theme(self):
        fg, border, bg = self.colours()
        self.styles.background = bg
        for w in self.query("*"):
            try:
                w.styles.color = fg
                w.styles.background = bg
            except Exception:
                pass
        for sel in ["#banner", "#left", "#middle", "#right", "#cmd"]:
            try:
                self.query_one(sel).styles.border = ("heavy" if sel in ["#banner", "#cmd"] else "round", border)
            except Exception:
                pass

    def animate(self):
        self.blink_on = not self.blink_on
        art = blink(self.gecko) if self.blink_on else self.gecko
        theme = self.theme_names[self.theme_idx].upper()
        self.query_one("#banner", Static).update(
            art + f"\n🦎 CONTROL • AUTOMATE • PROTECT • EXPLORE     THEME: {theme}     F5 SWITCH"
        )

    def refresh_panels(self):
        self.apply_theme()
        je_scans, tg_scans = scan_counts()
        procs = active_scan_processes()
        self.query_one("#left", Static).update(system_panel())
        self.query_one("#menuTitle", Static).update("« MAIN CONTROL MENU »     click item or type number")
        self.query_one("#firehose", Static).update(f"""
╔═ 🔥 MINI FIREHOSE / LIVE SCAN OPS ═╗

JE scans: {je_scans}     TG scans: {tg_scans}

{latest_scan_log()[:780]}
""")
        self.query_one("#right", Static).update(f"""
╔═ 🦎 GECK0 OPS STATUS ═╗

MODE            COMMAND
TIME            {datetime.now().strftime("%H:%M:%S")}
CYBERX          ● READY
CRUMBLE         ● READY
SEARCH          ◐ BOOTSTRAP
GRAPH           ○ PLANNED

╔═ 🛡 RUNNING SCANS ═╗

JE scans        {je_scans}
TG scans        {tg_scans}

{procs[:360]}

╔═ COMMANDS ═╗

scan trex mmcy.uk
show latest scan results
firehose
running scans
logs
search ketama
theme matrix
git status
""")

    def action_focus_cmd(self):
        self.query_one("#cmd", Input).focus()

    def action_refresh_panels(self):
        self.refresh_panels()

    def action_cycle_theme(self):
        self.theme_idx = (self.theme_idx + 1) % len(self.theme_names)
        self.refresh_panels()

    def on_button_pressed(self, event: Button.Pressed):
        label = str(event.button.label)
        self.query_one("#right", Static).update(f"SELECTED\n\n{label}\n\nType a command or click another module.")
        self.query_one("#cmd", Input).focus()

    def on_input_submitted(self, event: Input.Submitted):
        cmd = event.value.strip()
        event.input.value = ""
        if cmd in ("x", "q", "exit", "quit"):
            self.exit()
            return
        out = route(cmd)
        if out.startswith("__THEME__:"):
            wanted = out.split(":", 1)[1]
            if wanted in self.theme_names:
                self.theme_idx = self.theme_names.index(wanted)
                self.refresh_panels()
                return
        self.query_one("#right", Static).update(f"╔═ COMMAND OUTPUT ═╗\n\n{out[:1600]}")
        self.refresh_panels()

def main():
    Geck0LiveApp().run()

if __name__ == "__main__":
    main()
