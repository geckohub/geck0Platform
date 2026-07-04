from __future__ import annotations

import argparse
from .utils import root
from .backup import architecture_backup, backup_linode
from .release import make_release
from .tg import package_tg, write_bootstrap
from .verify import verify

def help_text() -> None:
    print("""
Geck0Deploy Python CLI

Commands:
  geck0 verify              Check Git, folders, executables, disk, Linode, TG queue
  geck0 status              Show basic platform status
  geck0 projects            Show registered Geck0verse projects
  geck0 new <name>          Create a new universal project
  geck0 pending             Show pending TG/update packages
  geck0 install             Install pending packages into JE tracking area
  geck0 release <name>      Create release package
  geck0 package-tg <name>   Queue TG update package
  geck0 tg-bootstrap        Write TG bootstrap script
  geck0 backup              Create Geck0Platform architecture backup
  geck0 backup-all          Backup all registered project architecture
  geck0 backup-linode       Upload latest architecture backup to Linode
  geck0 doctor              Run full health check
  geck0 publish "message"   Verify, backup, commit, and push
  geck0 help                Show this help
""")

def main() -> None:
    parser = argparse.ArgumentParser(prog="geck0", add_help=False)
    parser.add_argument("cmd", nargs="?", default="help")
    parser.add_argument("args", nargs="*")
    ns = parser.parse_args()

    cmd = ns.cmd
    args = ns.args

    if cmd == "help":
        help_text()
    elif cmd == "verify":
        verify()
    elif cmd == "backup":
        architecture_backup()
    elif cmd == "backup-linode":
        backup_linode()
    elif cmd == "release":
        make_release(args[0] if args else "geck0_release")
    elif cmd == "package-tg":
        package_tg(args[0] if args else "tg_update")
    elif cmd == "tg-bootstrap":
        write_bootstrap()
    elif cmd == "status":
        print(f"Geck0Deploy Python root: {root()}")
    elif cmd == "projects":
        from . import projects
        projects.main(args)
    elif cmd == "new":
        from . import new_project
        new_project.main(args)
    elif cmd == "pending":
        from . import install
        install.pending()
    elif cmd == "install":
        from . import install
        install.install()
    elif cmd == "backup-all":
        from . import registry_backup
        registry_backup.main(args)
    elif cmd == "doctor":
        from . import doctor
        doctor.main(args)
    elif cmd == "publish":
        from . import publish
        publish.main(args)
    else:
        print(f"Unknown command: {cmd}")
        help_text()

if __name__ == "__main__":
    main()
