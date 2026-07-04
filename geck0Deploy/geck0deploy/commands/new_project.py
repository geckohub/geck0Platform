from pathlib import Path
import shutil
from geck0deploy.core.config import root, workspace
from geck0deploy.core.shell import run
from geck0deploy.core.registry import ensure_default_registry


def main(args=None):
    args = args or []
    if not args:
        print('Usage: geck0 new <project_name>')
        return
    name = args[0]
    pretty = name.replace('_',' ').replace('-',' ').title()
    target = workspace() / name
    template = root() / 'geck0Deploy' / 'templates' / 'universal_project'
    if target.exists():
        print(f'Project already exists: {target}')
        return
    if not template.exists():
        print(f'Missing template: {template}')
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(template, target)
    readme = target / 'README.md'
    if readme.exists():
        readme.write_text(readme.read_text().replace('PROJECT_NAME', pretty))
    meta = target / 'geck0project.yaml'
    meta.write_text(f'''project:\n  name: {name}\n  display_name: {pretty}\n  family: {name}\n  host: JE\n  status: active\nbackup:\n  architecture: true\n  include_large_files: false\n''')
    run(['git','init'], cwd=target)
    run(['git','add','.'], cwd=target)
    run(['git','commit','-m',f'Initial {pretty} project structure'], cwd=target)
    print(f'Created project: {target}')
    ensure_default_registry()
