from pathlib import Path
import shutil
import subprocess
import sys

from .utils import root

def main(args):
    if not args:
        print("Usage: geck0 new <project_name>")
        return

    name = args[0]
    pretty = name.replace("_", " ").replace("-", " ").title()
    workspace = Path.home() / "geck0Projects"
    template = root() / "geck0Deploy" / "templates" / "universal_project"
    target = workspace / name

    if target.exists():
        print(f"Project already exists: {target}")
        return

    workspace.mkdir(parents=True, exist_ok=True)

    if not template.exists():
        print(f"Template missing: {template}")
        sys.exit(1)

    shutil.copytree(template, target)

    readme = target / "README.md"
    if readme.exists():
        readme.write_text(readme.read_text().replace("PROJECT_NAME", pretty))

    subprocess.run(["git", "init"], cwd=target, check=False)
    subprocess.run(["git", "add", "."], cwd=target, check=False)
    subprocess.run(["git", "commit", "-m", f"Initial {pretty} project structure"], cwd=target, check=False)

    print(f"Created project: {target}")
    print()
    print("Next:")
    print(f"  cd {target}")
    print("  git status")
