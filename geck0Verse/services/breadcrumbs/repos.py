from pathlib import Path
import re,subprocess,yaml,os
ROOT=Path(os.getenv("BREADCRUMBS_PROJECT_ROOT","/workspace/geck0Projects/pinkGeck0/breadCrumbs/clients"))
def slugify(name):
    slug=re.sub(r"[^a-z0-9]+","-",name.casefold()).strip("-")
    if not slug:raise ValueError("Invalid project name")
    return slug[:64]
def path_for(name):
    root=ROOT.resolve();p=(root/slugify(name)).resolve()
    if root not in p.parents:raise ValueError("Unsafe path")
    return p
def init_repo(name,template="static-site"):
    p=path_for(name)
    if p.exists() and any(p.iterdir()):raise FileExistsError(str(p))
    p.mkdir(parents=True,exist_ok=True);(p/"README.md").write_text(f"# {name}\n\nCreated by BreadCrumbs.\n");(p/"project.yaml").write_text(yaml.safe_dump({"project":{"name":name,"slug":p.name,"template":template,"parent":"pinkGeck0/breadCrumbs"}}));(p/"manifest.json").write_text('{"created_by":"BreadCrumbs","version":"0.1.0"}\n')
    for d in ["src","docs","governance"]:(p/d).mkdir()
    subprocess.run(["git","init","-b","main"],cwd=p,check=False,capture_output=True);subprocess.run(["git","add","."],cwd=p,check=False,capture_output=True);subprocess.run(["git","-c","user.name=BreadCrumbs","-c","user.email=breadcrumbs@local","commit","-m","Initial BreadCrumbs project"],cwd=p,check=False,capture_output=True);return p
def commit(name,message):
    p=path_for(name);subprocess.run(["git","add","."],cwd=p,check=True);r=subprocess.run(["git","-c","user.name=BreadCrumbs","-c","user.email=breadcrumbs@local","commit","-m",message],cwd=p,capture_output=True,text=True);return {"returncode":r.returncode,"stdout":r.stdout,"stderr":r.stderr}
