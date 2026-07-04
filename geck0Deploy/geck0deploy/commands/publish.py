import datetime
from geck0deploy.core.config import root
from geck0deploy.core.shell import run
from geck0deploy.commands import verify, backup


def main(args=None):
    msg = ' '.join(args or []) or f'Geck0 publish {datetime.datetime.now():%Y-%m-%d %H:%M}'
    print('Geck0Deploy Publish')
    verify.main([])
    backup.backup_all([])
    run(['git','add','.'], cwd=root())
    res = run(['git','commit','-m',msg], cwd=root())
    if res.returncode != 0:
        print('No commit created; likely nothing changed.')
    run(['git','push'], cwd=root())
    print('Publish complete.')
