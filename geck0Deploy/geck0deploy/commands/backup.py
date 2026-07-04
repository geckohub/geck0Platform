from pathlib import Path
import tarfile
from geck0deploy.core.config import root, linode_user, linode_host, linode_dir
from geck0deploy.core.archive import add_tree, timestamp
from geck0deploy.core.registry import ensure_default_registry, load_projects
from geck0deploy.core.shell import run


def architecture_backup(args=None):
    out_dir = Path.home() / 'geck0_architecture_backups'
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f'geck0verse_architecture_{timestamp()}.tar.gz'
    with tarfile.open(out, 'w:gz') as tar:
        add_tree(tar, root(), 'geck0Platform')
    print(f'Created architecture backup: {out}')


def backup_all(args=None):
    ensure_default_registry()
    out_dir = Path.home() / 'geck0_architecture_backups'
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f'geck0verse_registry_architecture_{timestamp()}.tar.gz'
    projects = load_projects()
    with tarfile.open(out, 'w:gz') as tar:
        for name, meta in projects.items():
            if str(meta.get('backup','true')).lower() == 'false':
                continue
            add_tree(tar, Path(meta.get('path','')).expanduser(), name)
    print(f'Created registry architecture backup: {out}')


def backup_linode(args=None):
    architecture_backup([])
    out_dir = Path.home() / 'geck0_architecture_backups'
    latest = sorted(out_dir.glob('*.tar.gz'), key=lambda p: p.stat().st_mtime)[-1]
    dest = f'{linode_user()}@{linode_host()}:{linode_dir()}/'
    run(['ssh',f'{linode_user()}@{linode_host()}',f'mkdir -p {linode_dir()}'], check=False)
    run(['scp',str(latest),dest], check=False)
    print(f'Uploaded: {latest.name}')
