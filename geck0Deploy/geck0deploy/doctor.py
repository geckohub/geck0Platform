from . import verify, projects, registry_backup

def main(args):
    print("Geck0Deploy Doctor")
    print("==================")
    print()

    print("## Verify")
    verify.main([])
    print()

    print("## Projects")
    projects.main([])
    print()

    print("## Backup Test")
    registry_backup.main([])
    print()

    print("Doctor complete.")
