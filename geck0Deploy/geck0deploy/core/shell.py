import subprocess
from pathlib import Path


def run(cmd, cwd=None, check=False):
    print("$ " + " ".join(str(c) for c in cmd))
    return subprocess.run([str(c) for c in cmd], cwd=cwd, check=check)


def capture(cmd, cwd=None):
    return subprocess.run([str(c) for c in cmd], cwd=cwd, text=True, capture_output=True)
