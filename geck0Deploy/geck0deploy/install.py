from pathlib import Path
import tarfile
import zipfile
import shutil
from .utils import root

def pending():
    pending_dir = root() / "governance" / "tg" / "pending_updates"
    pending_dir.mkdir(parents=True, exist_ok=True)

    print("Pending Geck0/TG update packages:")
    for p in sorted(pending_dir.iterdir()):
        if p.is_file():
            print(f"  {p.name}  ({p.stat().st_size} bytes)")

def install():
    pending_dir = root() / "governance" / "tg" / "pending_updates"
    installed_dir = root() / "governance" / "tg" / "applied_updates"
    installed_dir.mkdir(parents=True, exist_ok=True)

    print("Installing pending packages into JE tracking area...")

    for pkg in sorted(pending_dir.iterdir()):
        if not pkg.is_file():
            continue

        marker = installed_dir / f"{pkg.name}.done"
        if marker.exists():
            print(f"SKIP already installed: {pkg.name}")
            continue

        target = installed_dir / pkg.stem
        target.mkdir(parents=True, exist_ok=True)

        if pkg.suffix == ".zip":
            with zipfile.ZipFile(pkg, "r") as z:
                z.extractall(target)
        elif pkg.name.endswith(".tar.gz"):
            with tarfile.open(pkg, "r:gz") as t:
                t.extractall(target)
        else:
            shutil.copy2(pkg, target / pkg.name)

        marker.write_text("installed\n")
        print(f"INSTALLED: {pkg.name}")

    print("Install complete.")
