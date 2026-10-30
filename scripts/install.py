import argparse
from datetime import datetime, timezone
import filecmp
import os
from pathlib import Path
import shutil
import sys
import tempfile
import uuid


def same_contents(source, target):
    if not target.is_dir():
        return False
    comparison = filecmp.dircmp(source, target)
    if comparison.left_only or comparison.right_only or comparison.common_funny:
        return False
    _, different, errors = filecmp.cmpfiles(
        source, target, comparison.common_files, shallow=False
    )
    return not different and not errors and all(
        same_contents(source / name, target / name) for name in comparison.common_dirs
    )


def install_one(source, target, replace, backup_root):
    exists = target.exists() or target.is_symlink()
    if exists and same_contents(source, target):
        return "unchanged"
    if exists and not replace:
        return "skipped"
    with tempfile.TemporaryDirectory(prefix=".skill-install-", dir=target.parent.parent) as temp:
        staged = Path(temp) / source.name
        shutil.copytree(source, staged, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        backup = backup_root / source.name if exists else None
        if backup is not None:
            backup.parent.mkdir(parents=True, exist_ok=True)
            target.rename(backup)
        try:
            os.replace(staged, target)
        except OSError:
            if backup is not None:
                backup.rename(target)
            raise
    return "updated" if exists else "installed"


def install(source_root, destination, replace=False, names=None):
    source_root = Path(source_root).resolve()
    destination = Path(destination).expanduser().absolute()
    available = {
        path.name: path
        for path in source_root.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    }
    selected = sorted(set(names) if names else available)
    unknown = set(selected) - available.keys()
    if unknown:
        raise ValueError("Unknown skills: " + ", ".join(sorted(unknown)))
    if not selected:
        raise ValueError("No skills found in the source directory")
    if any(destination.resolve().is_relative_to(path.resolve()) for path in available.values()):
        raise ValueError("The destination must be outside source skill directories")
    destination.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
    backup_root = destination.parent / "skill-backups" / f"{stamp}-{uuid.uuid4().hex[:8]}"
    return {
        name: install_one(available[name], destination / name, replace, backup_root)
        for name in selected
    }


def main():
    parser = argparse.ArgumentParser(description="Install the repository's agent skills safely.")
    parser.add_argument("--target", type=Path, default=Path.home() / ".agents" / "skills")
    parser.add_argument("--only", nargs="+", help="Install only the named skills.")
    parser.add_argument("--replace", action="store_true", help="Back up and replace differing installs.")
    args = parser.parse_args()
    source_root = Path(__file__).resolve().parents[1] / "skills"
    try:
        results = install(source_root, args.target, args.replace, args.only)
    except (OSError, ValueError) as error:
        print(f"Installation failed: {error}", file=sys.stderr)
        return 1
    for name, status in results.items():
        print(f"{status}: {name}")
    print(f"Skills directory: {args.target.expanduser().absolute()}")
    print("Existing differences are skipped unless --replace is supplied.")
    print(f"Backups when replacing: {args.target.expanduser().absolute().parent / 'skill-backups'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
