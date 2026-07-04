from pathlib import Path
import os


def root() -> Path:
    return Path(os.environ.get("GECK0_ROOT", Path.home() / "geck0Platform")).expanduser()


def workspace() -> Path:
    return Path(os.environ.get("GECK0_WORKSPACE", Path.home() / "geck0Projects")).expanduser()


def linode_user() -> str:
    return os.environ.get("GECK0_LINODE_USER", "pinkgeck0")


def linode_host() -> str:
    return os.environ.get("GECK0_LINODE_HOST", "172.233.15.159")


def linode_dir() -> str:
    return os.environ.get("GECK0_LINODE_DIR", "/home/pinkgeck0/backups/software_architecture")
