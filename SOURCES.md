# Sources and portability

## Included snapshots

This repository contains 51 unique personal skills copied from the installed
`~/.codex/skills` and `~/.agents/skills` collections on 2026-10-31. The duplicate
`auto-commit-task` installation was resolved to one copy. The two original OS
maintenance skills bring the total to 53; see [CATALOG.md](CATALOG.md).

All supporting files are included, excluding Git metadata, Python caches, and
desktop junk. Runtime source, data, attribution, and license declarations retain
their original layout; upstream-only maintenance tests are described below.
Newly authored installer/test files follow the repository's 150-line rule.

ECC specialist and command references came from the installed
[Everything Claude Code fork](https://github.com/worldflowai/everything-claude-code)
at revision `37d60d841a2b6709c3a18f67c69e5ab193934fa6`.
Other collections are snapshots of the available personal installation; no
unverified upstream version or blanket repository license is asserted for them.
UI/UX data retains its bundled provenance and licensing metadata.

## Adaptations

- Every `ecc-*` wrapper bundles its actual profile/command and shared workflow in
  `references/`, replacing links to the original machine's absolute home path.
- Shared ECC guidance refers to installed skill names and current host/user rules.
- UI/UX command examples resolve the current skill directory instead of assuming
  a Claude plugin path. Its Python implementation and data are retained.
- Ponytail's argument hint is preserved as metadata compatible with skill validation.
  Help uses the installed skill names; plugin-only extras remain identified.
- Angular compatibility metadata and Next.js description markup are normalized
  for the same skill validator without changing their workflow instructions.
- Two upstream-only UI/UX maintenance test modules are retained under
  references/upstream-maintenance/, with their missing upstream tool dependencies
  documented there. The deployed search/data regression suite remains runnable.
- Trailing whitespace in two imported ECC references and the UI/UX design-system
  helper is normalized; the helper's runtime regression tests cover the result.
- Installation uses portable Python copies rather than requiring symlinks,
  junction permissions, Bash, or a platform-specific package manager.

## Runtime requirements

| Collection | Requirements and limits |
| --- | --- |
| Architecture, patterns, review, planning | A coding agent and access to the target project's files/tools. |
| UI/UX Pro Max | Python and included scripts/data; no external search package is needed. |
| Angular / Next.js | Framework, package manager, and versions required by the chosen skill. |
| Next dev loop | A running supported Next.js dev server and the browser/MCP tools named in that skill. |
| Graphify | Its external Graphify CLI/Python package; copying instructions does not install that runtime. |
| Learning/compaction hook helpers | Compatible Claude Code hook configuration and Bash; some also need `jq`. |
| Ponytail plugin extras | The original plugin for band/update controls; benchmark figures are upstream claims. |
| OS maintenance | Native OS tools and an installed client such as Happ when needed. |

The installer never enables hooks, installs runtimes, changes model settings,
starts agents/services, or connects account integrations. Built-in system skills
and connected-plugin skills remain host-managed instead of being copied from
their package caches.

The collection and installer are verified on Linux. Windows and macOS native
systems were unavailable for execution here. Framework workflows still need
validation in their target projects.
