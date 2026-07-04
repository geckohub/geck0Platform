import re
from .scans import latest_scan_results, launch_scan, active_scan_processes, latest_scan_log
from .utils import sh, GECK0_HOME

MENU_MAP = {
    "01": "BlackGeck0", "1": "BlackGeck0", "black": "BlackGeck0",
    "02": "GreenGeck0", "2": "GreenGeck0", "green": "GreenGeck0",
    "03": "PinkGeck0", "3": "PinkGeck0", "pink": "PinkGeck0",
    "04": "BlueGeck0", "4": "BlueGeck0", "blue": "BlueGeck0",
    "05": "YellowGeck0", "5": "YellowGeck0", "yellow": "YellowGeck0",
    "06": "PurpleGeck0", "6": "PurpleGeck0", "purple": "PurpleGeck0",
    "07": "Crumble", "7": "Crumble", "crumble": "Crumble",
    "08": "CyberX", "8": "CyberX", "cyberx": "CyberX",
    "09": "Geck0 Search", "9": "Geck0 Search", "search": "Geck0 Search",
    "10": "Geck0Report", "report": "Geck0Report",
    "11": "Knowledge Graph", "graph": "Knowledge Graph",
    "12": "Dashboard", "dashboard": "Dashboard",
    "13": "Wiki", "wiki": "Wiki",
    "14": "Git", "git": "Git",
}

def parse_scan(text: str):
    parts = text.split()
    profile = "trex"
    target = ""
    for p in parts[1:]:
        if p in ("trex", "full", "quick", "lite", "verbose"):
            profile = p
        elif "." in p:
            target = p
    return target, profile

def route(text: str):
    q = text.strip()
    low = q.lower().strip()

    if low in ("",):
        return "No command."
    if low in MENU_MAP:
        return f"Selected module: {MENU_MAP[low]}\n\nFuture: open dedicated module screen."

    if low.startswith("theme "):
        return "__THEME__:" + low.split(" ", 1)[1].strip()

    if low.startswith("scan "):
        target, profile = parse_scan(low)
        return launch_scan(target, profile)

    if "latest scan" in low or "scan result" in low or "latest result" in low:
        return "LATEST SCAN RESULTS\n\n" + latest_scan_results()

    if "running scan" in low or "scan process" in low or low == "processes":
        return "RUNNING SCAN PROCESSES\n\n" + active_scan_processes()

    if "firehose" in low or "scan logs" in low or low == "logs":
        return "LIVE FIREHOSE\n\n" + latest_scan_log()

    if low.startswith("git"):
        args = q[3:].strip() or "status"
        return sh(f"git -C {GECK0_HOME} {args}", 6)

    if low.startswith("search "):
        query = q.split(" ", 1)[1]
        return f"GECK0 SEARCH\n\nQuery: {query}\n\nFuture: search wiki, logs, scans, files, voice, notes and graph."

    if low.startswith("report"):
        return f"GECK0REPORT\n\nCommand: {q}\n\nFuture: generate/open report workflow."

    return f"Command accepted: {q}\n\nNo concrete route yet. Try: scan trex mmcy.uk, show latest scan results, firehose, logs, git status."
