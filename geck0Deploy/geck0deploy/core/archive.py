from pathlib import Path
import tarfile
import datetime

EXCLUDE_NAMES = {'.git','__pycache__','.venv','venv','node_modules','logs','reports','storage','updates','backups','clients','client','evidence','screenshots'}
EXCLUDE_SUFFIXES = ('.pyc','.tar.gz','.zip','.mp4','.mov','.mkv','.iso')


def skip(path: Path) -> bool:
    return path.name in EXCLUDE_NAMES or str(path).endswith(EXCLUDE_SUFFIXES)


def add_tree(tar: tarfile.TarFile, src: Path, arc_prefix: str):
    if not src.exists():
        print(f"SKIP missing: {src}")
        return
    for item in src.rglob('*'):
        if any(skip(part) for part in item.parents) or skip(item):
            continue
        tar.add(item, arcname=Path(arc_prefix) / item.relative_to(src), recursive=False)


def timestamp() -> str:
    return datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
