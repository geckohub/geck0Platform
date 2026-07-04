from pathlib import Path
from geck0deploy.core.config import root, linode_host, linode_user
from geck0deploy.core.shell import run
from geck0deploy.core.registry import ensure_default_registry, load_projects


def main(args=None):
    r = root()
    print('Geck0Deploy v1.0 Verify')
    print('=======================')
    print(f'Root: {r}\n')
    print('[Git]')
    run(['git','status','--short'], cwd=r)
    run(['git','remote','-v'], cwd=r)
    print('\n[Required folders]')
    for rel in ['governance','governance/tg','governance/tg/pending_updates','geck0Deploy','geck0Deploy/docs']:
        p = r / rel
        print(('OK: ' if p.exists() else 'MISSING: ') + rel)
    print('\n[Executables]')
    for rel in ['geck0Deploy/bin/geck0','geck0Deploy/bin/geck0-py']:
        p = r / rel
        print(('OK: ' if p.exists() and p.stat().st_mode & 0o111 else 'MISSING/not executable: ') + rel)
    print('\n[Registry]')
    ensure_default_registry()
    projects = load_projects()
    print(f'Projects registered: {len(projects)}')
    print('\n[Disk]')
    run(['df','-h','/'])
    print('\n[Linode SSH]')
    res = run(['ssh','-o','BatchMode=yes','-o','ConnectTimeout=8',f'{linode_user()}@{linode_host()}','echo OK'])
    print('OK: Linode SSH works' if res.returncode == 0 else 'WARN: Linode SSH not passwordless yet')
    print('\n[TG Queue]')
    q = r / 'governance' / 'tg' / 'pending_updates'
    q.mkdir(parents=True, exist_ok=True)
    for item in sorted(q.iterdir()):
        if item.is_file():
            print(item.name)
