from geck0deploy.commands import verify, projects, backup


def main(args=None):
    print('Geck0Deploy v1.0 Doctor')
    print('=======================')
    verify.main([])
    print('\n[Projects]')
    projects.main([])
    print('\n[Backup smoke test]')
    backup.backup_all([])
    print('\nDoctor complete.')
