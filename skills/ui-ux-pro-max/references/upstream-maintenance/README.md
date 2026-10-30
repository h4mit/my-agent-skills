# Upstream maintenance test references

These original test modules are preserved for maintaining the upstream catalog
and relevance benchmark. They require utilities from the complete upstream
repository that were not present in the installed skill snapshot:

- test_catalog_refresh.py: scripts/refresh-google-fonts.py and scripts/refresh-icon-catalog.py.
- test_relevance_evaluator.py: scripts/evaluate-relevance.py and its upstream source layout.

They are reference material, separate from the deployed runtime regression suite.
Restore them to their original scripts/tests location in a matching complete
upstream checkout when working on those maintenance utilities. Their original
fixtures remain bundled under this skill's scripts/tests/fixtures directory.

To test the portable search runtime and included data from this repository, run:

```sh
python3 -m unittest discover -s skills/ui-ux-pro-max/scripts/tests
```

The installer and skill validation are tested separately from the repository root.
