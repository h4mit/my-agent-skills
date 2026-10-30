import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "install.py"
SPEC = importlib.util.spec_from_file_location("skill_install", SCRIPT)
INSTALLER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(INSTALLER)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.target = self.root / "personal" / "skills"
        for name in ("architecture", "testing"):
            folder = self.source / name
            folder.mkdir(parents=True)
            (folder / "SKILL.md").write_text(f"Skill {name}\n", encoding="utf-8")
            (folder / "references").mkdir()
            (folder / "references" / "guide.md").write_text("Guide\n", encoding="utf-8")

    def test_installs_all_assets_and_leaves_unrelated_skills(self):
        unrelated = self.target / "my-existing-skill"
        unrelated.mkdir(parents=True)
        (unrelated / "SKILL.md").write_text("Keep me", encoding="utf-8")
        results = INSTALLER.install(self.source, self.target)
        self.assertEqual(set(results.values()), {"installed"})
        self.assertEqual((self.target / "testing/references/guide.md").read_text(), "Guide\n")
        self.assertEqual((unrelated / "SKILL.md").read_text(), "Keep me")

    def test_rerun_is_unchanged_without_backups(self):
        INSTALLER.install(self.source, self.target)
        results = INSTALLER.install(self.source, self.target, replace=True)
        self.assertEqual(set(results.values()), {"unchanged"})
        self.assertFalse((self.target.parent / "skill-backups").exists())

    def test_existing_changes_are_skipped_by_default(self):
        INSTALLER.install(self.source, self.target)
        file = self.target / "architecture/SKILL.md"
        file.write_text("My customization", encoding="utf-8")
        results = INSTALLER.install(self.source, self.target)
        self.assertEqual(results["architecture"], "skipped")
        self.assertEqual(file.read_text(), "My customization")

    def test_replace_keeps_backup_outside_active_skills(self):
        INSTALLER.install(self.source, self.target)
        file = self.target / "architecture/SKILL.md"
        file.write_text("My customization", encoding="utf-8")
        results = INSTALLER.install(self.source, self.target, replace=True)
        backups = list((self.target.parent / "skill-backups").glob("*/architecture/SKILL.md"))
        self.assertEqual(results["architecture"], "updated")
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_text(), "My customization")
        self.assertEqual(file.read_text(), "Skill architecture\n")

    def test_copy_failure_preserves_existing_install(self):
        INSTALLER.install(self.source, self.target)
        file = self.target / "architecture/SKILL.md"
        file.write_text("Keep this version", encoding="utf-8")
        with patch.object(INSTALLER.shutil, "copytree", side_effect=OSError("disk full")):
            with self.assertRaises(OSError):
                INSTALLER.install(self.source, self.target, replace=True)
        self.assertEqual(file.read_text(), "Keep this version")

    def test_failed_activation_restores_previous_install(self):
        INSTALLER.install(self.source, self.target)
        file = self.target / "architecture/SKILL.md"
        file.write_text("Keep this version", encoding="utf-8")
        with patch.object(INSTALLER.os, "replace", side_effect=OSError("activation failed")):
            with self.assertRaises(OSError):
                INSTALLER.install(self.source, self.target, replace=True)
        self.assertEqual(file.read_text(), "Keep this version")

    def test_selection_and_unknown_name_validation(self):
        results = INSTALLER.install(self.source, self.target, names=["testing"])
        self.assertEqual(results, {"testing": "installed"})
        self.assertFalse((self.target / "architecture").exists())
        with self.assertRaises(ValueError):
            INSTALLER.install(self.source, self.target, names=["../outside"])

    def test_refuses_installation_inside_a_source_skill(self):
        with self.assertRaises(ValueError):
            INSTALLER.install(self.source, self.source / "testing/nested")
        self.assertFalse((self.source / "testing/nested").exists())

    def test_cli_reports_invalid_selection_without_writes(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--target", str(self.target), "--only", "unknown"],
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Unknown skills", result.stderr)
        self.assertFalse(self.target.exists())


if __name__ == "__main__":
    unittest.main()
