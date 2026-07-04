from pathlib import Path
import tarfile
from geck0deploy.core.config import root
from geck0deploy.core.archive import timestamp, add_tree


def package_tg(args=None):
    args = args or []
    name = args[0] if args else 'tg_update'
    r = root()
    out_dir = r / 'governance' / 'tg' / 'pending_updates'
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f'{timestamp()}_{name}.tar.gz'
    with tarfile.open(out, 'w:gz') as tar:
        for rel in ['geck0Deploy','governance','scripts','config','geck0Docs']:
            p = r / rel
            if p.exists():
                add_tree(tar, p, rel)
    print(f'Queued TG package: {out}')


def bootstrap(args=None):
    r = root()
    b = r / 'governance' / 'tg' / 'bootstrap' / 'geck0_tg_bootstrap.sh'
    b.parent.mkdir(parents=True, exist_ok=True)
    b.write_text('''#!/usr/bin/env bash\nset -euo pipefail\nmkdir -p "$HOME/geck0Platform_tg_updates"/{incoming,applied,logs}\ncat > "$HOME/geck0Platform_tg_updates/geck0_tg_pull_updates.sh" <<'EOS'\n#!/usr/bin/env bash\nset -euo pipefail\nJE_HOST="lucy@192.168.1.244"\nJE_PORT="1991"\nREMOTE_DIR="/home/lucy/geck0Platform/governance/tg/pending_updates"\nLOCAL_IN="$HOME/geck0Platform_tg_updates/incoming"\nLOCAL_APPLIED="$HOME/geck0Platform_tg_updates/applied"\nLOG="$HOME/geck0Platform_tg_updates/logs/pull_$(date +%Y%m%d_%H%M%S).log"\nmkdir -p "$LOCAL_IN" "$LOCAL_APPLIED" "$(dirname "$LOG")"\nrsync -avz -e "ssh -p $JE_PORT" "$JE_HOST:$REMOTE_DIR/" "$LOCAL_IN/" | tee -a "$LOG"\nfor pkg in "$LOCAL_IN"/*; do\n  [ -e "$pkg" ] || continue\n  base="$(basename "$pkg")"\n  [ -f "$LOCAL_APPLIED/$base.done" ] && continue\n  case "$pkg" in\n    *.tar.gz) tar -xzf "$pkg" -C "$HOME" ;;\n    *.zip) unzip -o "$pkg" -d "$HOME/geck0Platform_tg_updates/incoming/$base.extract" ;;\n  esac\n  touch "$LOCAL_APPLIED/$base.done"\ndone\nEOS\nchmod +x "$HOME/geck0Platform_tg_updates/geck0_tg_pull_updates.sh"\necho "TG bootstrap complete"\n''')
    b.chmod(0o755)
    print(f'Wrote TG bootstrap: {b}')


def pending(args=None):
    q = root() / 'governance' / 'tg' / 'pending_updates'
    q.mkdir(parents=True, exist_ok=True)
    print('Pending TG/update packages:')
    for p in sorted(q.iterdir()):
        if p.is_file(): print(f'  {p.name} ({p.stat().st_size} bytes)')


def install(args=None):
    import zipfile, shutil
    q = root() / 'governance' / 'tg' / 'pending_updates'
    a = root() / 'governance' / 'tg' / 'applied_updates'
    a.mkdir(parents=True, exist_ok=True)
    for pkg in sorted(q.iterdir()):
        if not pkg.is_file(): continue
        marker = a / f'{pkg.name}.done'
        if marker.exists():
            print(f'SKIP: {pkg.name}')
            continue
        target = a / pkg.name.replace('.tar.gz','').replace('.zip','')
        target.mkdir(parents=True, exist_ok=True)
        if pkg.name.endswith('.tar.gz'):
            with tarfile.open(pkg,'r:gz') as tar: tar.extractall(target)
        elif pkg.name.endswith('.zip'):
            with zipfile.ZipFile(pkg) as z: z.extractall(target)
        else:
            shutil.copy2(pkg, target / pkg.name)
        marker.write_text('installed\n')
        print(f'INSTALLED: {pkg.name}')
