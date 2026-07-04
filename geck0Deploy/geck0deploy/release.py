from __future__ import annotations

import json
import tarfile
from pathlib import Path
from .utils import root, ensure_dir, now_stamp


def make_release(name: str) -> Path:
    r = root()
    stamp = now_stamp()
    rel_dir = r / "geck0Deploy" / "releases" / f"{stamp}_{name}"
    ensure_dir(rel_dir)
    manifest = {
        "name": name,
        "created": stamp,
        "type": "geck0deploy_release",
        "version": "0.2.0",
        "targets": ["JE", "TG", "Mac", "Linode"],
    }
    (rel_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    (rel_dir / "RELEASE_NOTES.md").write_text(f"# Release Notes: {name}\n\nDate: {stamp}\n\n## Summary\n\nTODO\n\n## Changed\n\nTODO\n")
    (rel_dir / "CHANGELOG.md").write_text(f"# Changelog: {name}\n\n- TODO\n")
    (rel_dir / "BUILD_GUIDE.md").write_text(f"# Build Guide: {name}\n\n## Install\n\nTODO\n\n## Verify\n\nTODO\n")
    archive = rel_dir.with_suffix(".tar.gz")
    with tarfile.open(archive, "w:gz") as tf:
        tf.add(rel_dir, arcname=rel_dir.name)
    tgq = r / "governance" / "tg" / "pending_updates"
    ensure_dir(tgq)
    tg_copy = tgq / archive.name
    tg_copy.write_bytes(archive.read_bytes())
    print(f"Created release: {archive}")
    print(f"Queued for TG: {tg_copy}")
    return archive
