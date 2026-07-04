import services.breadcrumbs.repos as repos
def test_slug():assert repos.slugify("My Cool Site!")=="my-cool-site"
def test_init_repo(tmp_path,monkeypatch):
 monkeypatch.setattr(repos,"ROOT",tmp_path);p=repos.init_repo("Client Site");assert (p/"project.yaml").exists();assert (p/".git").exists()
