# My Agent Skills

A portable collection of **53 skills** for software development, architecture,
testing, code review, UI/UX, and selected OS maintenance tasks.

This includes all 51 personal skills from the installed development setup, plus
the two networking skills created here. Duplicate installation links are included
once, with their supporting files copied.

| Area | Examples |
| --- | --- |
| Architecture and planning | `ecc-architect`, `ecc-planner`, `ecc-plan`, `graphify` |
| Backend and data | `backend-patterns`, `clickhouse-io`, `security-review` |
| Frontend and UI/UX | `frontend-patterns`, `ui-ux-pro-max`, `coding-standards` |
| Angular | `angular-developer`, `angular-new-app` |
| Next.js | Cache Components adoption/optimization, partial prefetching, `next-dev-loop` |
| Testing and verification | `tdd-workflow`, `eval-harness`, `verification-loop`, ECC test/build profiles |
| Review and cleanup | ECC reviewers, Ponytail reviews/audits, refactoring and debt workflows |
| Development workflow | `ecc-workflow`, `auto-commit-task`, learning, checkpoints, documentation |
| OS maintenance | `os-network-repair`, `hiddify-uninstall` |

See the [complete skill catalog](CATALOG.md) for every skill and its purpose.

- [HELP.md](HELP.md): installation, updates, and rerunning tasks on each OS.
- [TIPS.md](TIPS.md): practical development and architecture workflows.
- [SOURCES.md](SOURCES.md): snapshot origins, portability adjustments, and dependencies.
- [Network tips](docs/NETWORK-TIPS.md): lessons from the original Happ/Hiddify repair.

## Quick setup

Clone this repository, then run its standard-library Python installer:

```sh
python3 scripts/install.py
```

On Windows, use `py -3 scripts/install.py`. Skills are copied into
`~/.agents/skills` by default. Existing differences are preserved unless
`--replace` is supplied; replacement creates backups outside the active skills
directory. Nothing installs global hooks, services, packages, or network settings.

ECC profiles include local references instead of depending on the original
machine's home directory. UI/UX search scripts and their data are included.
Built-in and connected-plugin skills remain managed by their respective hosts.

Installer tests and copied skill validation run on Linux. Windows and macOS
installation commands are documented but have not been executed on those systems.
