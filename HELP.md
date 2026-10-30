# Install and rerun the full skill collection

## Requirements

Install Git, Python 3.10 or newer, and your coding agent. The installer uses only
Python's standard library. Individual skills may need project tools listed in
their own instructions; see [SOURCES.md](SOURCES.md).

## Linux or macOS

For a new checkout:

```sh
(
  set -e
  git clone https://github.com/h4mit/my-agent-skills.git "$HOME/my-agent-skills"
  cd "$HOME/my-agent-skills"
  python3 scripts/install.py
)
```

If the checkout already exists, update it rather than cloning over it:

```sh
(
  set -e
  cd "$HOME/my-agent-skills"
  git pull --ff-only
  python3 scripts/install.py
)
```

## Windows

Use PowerShell for a new checkout:

```powershell
git clone https://github.com/h4mit/my-agent-skills.git "$HOME\my-agent-skills"
if ($LASTEXITCODE -ne 0) { throw 'Clone failed; use an existing checkout instead.' }
Set-Location "$HOME\my-agent-skills"
py -3 scripts/install.py
```

For an existing checkout:

```powershell
Set-Location "$HOME\my-agent-skills"
git pull --ff-only
if ($LASTEXITCODE -ne 0) { throw 'Update failed; resolve it before installing.' }
py -3 scripts/install.py
```

Use `python` instead of `py -3` if that is how Python is installed on the machine.

## Existing skills and updates

The installer discovers every folder containing `skills/NAME/SKILL.md`.
It copies the complete folder, including references, scripts, and data.

- `installed`: a new skill was copied.
- `unchanged`: the installed files already match.
- `skipped`: an existing installation differs and was preserved.
- `updated`: `--replace` was supplied, so the previous installation was backed up.

After reviewing local customizations, update differing copies with:

```sh
python3 scripts/install.py --replace
```

On Windows use `py -3` in place of `python3`. Backups are placed in
`~/.agents/skill-backups/TIMESTAMP-ID/`, outside the active skills directory.
Unrelated installed skills are left alone. Unchanged copies need no backup.
An installation failure restores the affected skill's previous copy; earlier
successfully installed skills remain installed.

Use `--target PATH` for a different destination. For example, Claude Code users
can target `~/.claude/skills`; this copies skills without enabling lifecycle hooks.
Installing skills does not grant permissions or connect external services.

To install a subset:

```sh
python3 scripts/install.py --only ecc-workflow ecc-architect backend-patterns
```

Restart the agent if new skills do not appear. Codex discovers user skills
under `~/.agents/skills`; see the [official skill documentation](https://developers.openai.com/codex/skills/).

## Rerun development and architecture work

Send the matching prompt to your agent in the target project:

```text
Use $ecc-architect to design this feature's software architecture.
Inspect the existing project, describe component boundaries and data flow,
and explain the important tradeoffs before implementation.
```

```text
Use $ecc-workflow and $backend-patterns to implement this backend change.
Follow the project's existing patterns, add proportionate regression tests,
verify the result, and use $auto-commit-task for the completed changes.
```

```text
Use $ponytail-review to review this change for correctness, security,
unnecessary complexity, and missing tests. Report findings before editing.
```

Choose framework skills such as `$angular-developer`, `$next-dev-loop`, or
`$ui-ux-pro-max` when the task fits. Read [CATALOG.md](CATALOG.md) for all 53 names
and [TIPS.md](TIPS.md) for combining them. Host-native tool names and plugin extras
in upstream examples do not install those tools or override your instructions.

## Rerun OS maintenance when needed

Use `$os-network-repair` with a privately supplied subscription for network work,
or `$hiddify-uninstall` to remove Hiddify while preserving profiles.
Platform details: [Linux](skills/os-network-repair/references/linux.md),
[macOS](skills/os-network-repair/references/macos.md),
[Windows](skills/os-network-repair/references/windows.md).
See [network tips](docs/NETWORK-TIPS.md) for the verified subscription format fix.
