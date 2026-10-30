# Development and architecture tips

## Start with the project and the problem

Use `$ecc-workflow` as the shared development guide. Read project instructions,
inspect the affected code and its callers, and run the project's existing checks.
Use `$graphify` when an existing project graph can explain relationships without
rebuilding an index unnecessarily.

## Choose the right architecture depth

Use `$ecc-architect` for boundaries, data flow, dependencies, reliability, and
tradeoffs. Use `$ecc-planner` or `$ecc-plan` when work needs an implementation
sequence. A small bug fix usually needs inspection and a regression check, not
a new architecture or abstraction.

Make the design concrete: identify the trigger, inputs, state ownership, failure
paths, and affected components. Keep decisions consistent with the existing
project unless the task calls for a change.

## Combine broad patterns with framework guidance

| Work | Useful skills |
| --- | --- |
| APIs and server behavior | `backend-patterns`, `security-review`, `coding-standards` |
| React/frontends | `frontend-patterns`, `coding-standards`, `ui-ux-pro-max` |
| Angular | `angular-developer`; `angular-new-app` for a new application |
| Next.js runtime behavior | `next-dev-loop` with the relevant cache/prefetch skill |
| Analytics/database work | `clickhouse-io` when ClickHouse is actually involved |

Skill availability does not mean every task needs every skill. Load instructions
that affect the requested work, preserving the user's chosen stack and tools.

## Verify what the user experiences

Use `$tdd-workflow` for meaningful behavior changes and `$verification-loop` for
final checks. `$ecc-build-error-resolver` and `$ecc-build-fix` target actual build
failures. `$eval-harness` is useful for capability/regression evaluations.

Use the project's checks and test the behavior that could break. For runtime or
interface changes, exercise the running application when the relevant workflow
requires it. Report checks that were unavailable instead of implying they passed.

## Review before committing

Use `$ponytail-review` or `$ecc-code-reviewer` for a change, and `$ponytail-audit`
for a requested whole-repository audit. Security review should cover the actual
inputs, permissions, and sensitive data affected by the change.

Keep the smallest complete solution. Preserve unrelated changes, inspect the
final diff, and use `$auto-commit-task` after successful verification. A local
commit does not authorize a push or Jira state change.

## Keep the collection portable

Run `scripts/install.py` from the checkout to install the full catalog. Use
`--only` for a subset and `--replace` after reviewing differing local copies.
Keep backups outside the active skill directory so old copies are not discovered
as duplicate skills. See [HELP.md](HELP.md) for commands on each OS.

Resolve script paths relative to the installed skill, not the current project.
External CLIs, browser tools, hook configurations, and plugin accounts remain
separate runtime requirements; see [SOURCES.md](SOURCES.md).

Keep credentials, project secrets, transcripts, and machine backups out of Git.
[Network troubleshooting notes](docs/NETWORK-TIPS.md) remain available for
Happ/Hiddify maintenance.
