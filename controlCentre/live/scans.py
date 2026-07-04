from pathlib import Path
from .utils import sh, tg

LOCAL_SCAN_ROOT = Path("/home/lucy/geckoscan1.0")

def scan_counts():
    je = sh("tmux ls 2>/dev/null | grep -c geck0scan || true")
    remote = tg("tmux ls 2>/dev/null | grep -c geck0scan || true")
    return je, remote

def active_scan_processes():
    local = sh("ps aux | egrep 'subfinder|httpx|katana|nuclei|ffuf|gobuster|nmap|geck0_v10_pipeline' | grep -v grep | head -8", 3)
    remote = tg("ps aux | egrep 'subfinder|httpx|katana|nuclei|ffuf|gobuster|nmap|geck0_v10_pipeline' | grep -v grep | head -8", 5)
    return local if local and local != "n/a" else remote

def latest_scan_log():
    cmd = "cd /home/lucy/geckoscan1.0 2>/dev/null && latest=$(find logs v9/output -type f \\( -name '*.log' -o -name '*.txt' -o -name '*.json' \\) 2>/dev/null | xargs -r ls -t | head -1); [ -n \"$latest\" ] && echo $latest && tail -n 12 \"$latest\""
    local = sh(cmd, 3)
    if local and local != "n/a":
        return "JE FIREHOSE\n" + local
    remote = tg(cmd, 6)
    if remote and remote != "n/a":
        return "TG FIREHOSE\n" + remote
    return "No firehose visible. Start a scan or unlock SSH key to ThaiGreen."

def latest_scan_results():
    cmd = "cd /home/lucy/geckoscan1.0 2>/dev/null && find v9/output -maxdepth 3 -type f \\( -name '*summary*' -o -name '*report*' -o -name '*.md' -o -name '*.pdf' \\) 2>/dev/null | xargs -r ls -t | head -15"
    local = sh(cmd, 3)
    if local and local != "n/a":
        return local
    remote = tg(cmd, 6)
    return remote if remote and remote != "n/a" else "No scan reports found."

def launch_scan(target: str, profile: str = "trex"):
    if not target:
        return "No target supplied. Try: scan trex mmcy.uk"
    stamp_cmd = "date +%Y%m%d_%H%M%S"
    stamp = sh(stamp_cmd)
    sess = f"geck0scan_{target.replace('.', '_')}_{profile}_{stamp}"
    cmd = (
        "cd /home/lucy/geckoscan1.0 && "
        f"tmux new-session -d -s {sess} "
        f"\\\"bash scripts/v10/geck0_v10_pipeline.sh {target} verbose {profile} "
        f"2>&1 | tee logs/pipeline/{sess}.log; echo; echo DONE; bash\\\" && echo {sess}"
    )
    out = tg(cmd, 8)
    if out and out != "n/a":
        return f"Started TG scan session: {out}"
    return "Could not start scan on ThaiGreen. SSH key may be locked or path/script unavailable."
