from __future__ import annotations

import argparse
from .backup import architecture_backup, backup_linode
from .release import make_release
from .tg import package_tg, write_bootstrap
from .verify import verify
from .utils import root


def main() -> None:
    parser = argparse.ArgumentParser(prog="geck0-py", description="Geck0Deploy Python CLI v0.2")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("verify")
    sub.add_parser("backup")
    sub.add_parser("backup-linode")
    rel = sub.add_parser("release")
    rel.add_argument("name", nargs="?", default="geck0_release")
    tg = sub.add_parser("package-tg")
    tg.add_argument("name", nargs="?", default="tg_update")
    sub.add_parser("tg-bootstrap")
    sub.add_parser("status")

    args = parser.parse_args()
    if args.cmd == "verify":
        verify()
    elif args.cmd == "backup":
        architecture_backup()
    elif args.cmd == "backup-linode":
        backup_linode()
    elif args.cmd == "release":
        make_release(args.name)
    elif args.cmd == "package-tg":
        package_tg(args.name)
    elif args.cmd == "tg-bootstrap":
        write_bootstrap()
    elif args.cmd == "status":
        print(f"Geck0Deploy Python v0.2 root: {root()}")
    else:
        parser.print_help()
