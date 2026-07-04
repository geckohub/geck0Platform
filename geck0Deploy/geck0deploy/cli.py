from __future__ import annotations
import sys
from geck0deploy import __version__
from geck0deploy.core.config import root

HELP = f'''
Geck0Deploy v{__version__}

Commands:
  geck0 help                Show this help
  geck0 status              Show root/version status
  geck0 verify              Check Git, folders, executables, disk, Linode, TG queue
  geck0 doctor              Run full health check and backup smoke test
  geck0 projects            Show registered Geck0verse projects
  geck0 new <name>          Create a new universal project
  geck0 backup              Create Geck0Platform architecture backup
  geck0 backup-all          Backup all registered project architecture
  geck0 backup-linode       Upload latest architecture backup to Linode
  geck0 release <name>      Create release package
  geck0 package-tg <name>   Queue TG update package
  geck0 tg-bootstrap        Write TG bootstrap script on JE
  geck0 pending             Show pending TG/update packages
  geck0 install             Install pending packages into JE tracking area
  geck0 publish "message"   Verify, backup, commit, and push
'''


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    cmd = argv[0] if argv else 'help'
    args = argv[1:]

    if cmd in ('help','-h','--help'):
        print(HELP)
    elif cmd == 'status':
        print(f'Geck0Deploy v{__version__} root: {root()}')
    elif cmd == 'verify':
        from geck0deploy.commands.verify import main as f; f(args)
    elif cmd == 'doctor':
        from geck0deploy.commands.doctor import main as f; f(args)
    elif cmd == 'projects':
        from geck0deploy.commands.projects import main as f; f(args)
    elif cmd == 'new':
        from geck0deploy.commands.new_project import main as f; f(args)
    elif cmd == 'backup':
        from geck0deploy.commands.backup import architecture_backup as f; f(args)
    elif cmd == 'backup-all':
        from geck0deploy.commands.backup import backup_all as f; f(args)
    elif cmd == 'backup-linode':
        from geck0deploy.commands.backup import backup_linode as f; f(args)
    elif cmd == 'release':
        from geck0deploy.commands.release import main as f; f(args)
    elif cmd == 'package-tg':
        from geck0deploy.commands.tg import package_tg as f; f(args)
    elif cmd == 'tg-bootstrap':
        from geck0deploy.commands.tg import bootstrap as f; f(args)
    elif cmd == 'pending':
        from geck0deploy.commands.tg import pending as f; f(args)
    elif cmd == 'install':
        from geck0deploy.commands.tg import install as f; f(args)
    elif cmd == 'publish':
        from geck0deploy.commands.publish import main as f; f(args)
    else:
        print(f'Unknown command: {cmd}')
        print(HELP)
        raise SystemExit(2)

if __name__ == '__main__':
    main()
