from pathlib import Path
import json
import tarfile
from geck0deploy.core.config import root
from geck0deploy.core.archive import timestamp


def main(args=None):
    args = args or []
    name = args[0] if args else 'geck0_release'
    r = root()
    rel_dir = r / 'geck0Deploy' / 'releases' / f'{timestamp()}_{name}'
    rel_dir.mkdir(parents=True, exist_ok=True)
    manifest = {'name': name, 'type': 'geck0deploy_release', 'created': timestamp(), 'root': str(r)}
    (rel_dir / 'manifest.json').write_text(json.dumps(manifest, indent=2))
    (rel_dir / 'RELEASE_NOTES.md').write_text(f'# Release Notes: {name}\n\n## Summary\n\nTODO\n')
    (rel_dir / 'CHANGELOG.md').write_text(f'# Changelog: {name}\n\n- TODO\n')
    (rel_dir / 'BUILD_GUIDE.md').write_text(f'# Build Guide: {name}\n\n## Install\n\nTODO\n')
    archive = rel_dir.with_suffix('.tar.gz')
    with tarfile.open(archive, 'w:gz') as tar:
        tar.add(rel_dir, arcname=rel_dir.name)
    print(f'Created release: {archive}')
