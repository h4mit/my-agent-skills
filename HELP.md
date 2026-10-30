# Install and rerun on your machines

## Install with an agent

In Codex on Linux, macOS, or Windows, send:

```text
Use $skill-installer to install these two skill folders from
https://github.com/h4mit/my-agent-skills:
skills/os-network-repair
skills/hiddify-uninstall
Preserve any existing local modifications.
```

If the skills do not appear, restart Codex. Personal skills can also be installed
in `~/.agents/skills`, which Codex discovers across projects. See the
[official OpenAI skill documentation](https://developers.openai.com/codex/skills/).

## Manual installation on Linux or macOS

Run in a terminal with Git installed. Choose a different checkout path if this
one already exists.

```sh
(
  set -e
  git clone https://github.com/h4mit/my-agent-skills.git "$HOME/my-agent-skills"
  cd "$HOME/my-agent-skills"
  mkdir -p "$HOME/.agents/skills"
  for name in os-network-repair hiddify-uninstall; do
    target="$HOME/.agents/skills/$name"
    if [ -e "$target" ] || [ -L "$target" ]; then
      printf 'Already installed: %s\n' "$target" >&2
      exit 1
    fi
    ln -s "$PWD/skills/$name" "$target"
  done
)
```

Keep the checkout at that location because the installed skills link to it.
Update with `git -C "$HOME/my-agent-skills" pull --ff-only`. Existing local
changes are preserved; resolve any Git conflict before retrying.

## Manual installation on Windows

Run in PowerShell with Git installed:

```powershell
git clone https://github.com/h4mit/my-agent-skills.git "$HOME\my-agent-skills"
if ($LASTEXITCODE -ne 0) { throw 'Clone failed; check the destination.' }
Set-Location "$HOME\my-agent-skills"
$skillsRoot = Join-Path $HOME '.agents\skills'
New-Item -ItemType Directory -Force -Path $skillsRoot | Out-Null
foreach ($name in @('os-network-repair', 'hiddify-uninstall')) {
    $target = Join-Path $skillsRoot $name
    if (Test-Path $target) { throw "Already installed: $target" }
    $source = (Resolve-Path "skills\$name").Path
    New-Item -ItemType Junction -Path $target -Target $source | Out-Null
}
```

Keep the checkout in place. Update with
`git -C "$HOME\my-agent-skills" pull --ff-only`.
If the filesystem does not support junctions, use `Copy-Item -Recurse` instead of
`New-Item -ItemType Junction`; copied installations need to be refreshed after
pulling updates. Back up old copies outside the active skills directory first.

## Rerun the network repair

Send this prompt on the machine needing repair:

```text
Use $os-network-repair to diagnose and fix this machine's networking.
Use my current Happ subscription, which I will provide privately.
Select a working server, route internet traffic through it with TUN,
and configure automatic connection at login.
Preserve other VPNs, Docker networks, profiles, and unrelated settings.
Verify DNS, routes, HTTPS, and the proxy exit before reporting success.
```

Provide the subscription in that private session when needed. The skill does not
remember a private URL from this repository or impose it on future sessions.
Describe the failing app or site if only part of the connection is broken.

For removal, send:

```text
Use $hiddify-uninstall to remove Hiddify from this machine.
Preserve saved profiles and settings, then verify that networking still works.
```

## Connect again without reinstalling the skills

Open Happ, select the compatible native subscription and a working server, then
connect. For all application traffic, use a verified TUN mode. Enable both login
startup and connection on launch; starting the window alone is insufficient.

| OS | Detailed steps |
| --- | --- |
| Linux desktop | [Diagnostics, Happ controls, and XDG autostart](skills/os-network-repair/references/linux.md) |
| macOS | [Diagnostics and Login Items](skills/os-network-repair/references/macos.md) |
| Windows | [Diagnostics and Startup shortcuts](skills/os-network-repair/references/windows.md) |

Automatic connection at login does not enforce a kill switch or guarantee a
connection before login. Test the next actual login separately.

## Undo a repair

Disconnect Happ first, remove only the startup entry created by the repair, and
restore the recorded proxy/DNS settings if needed. Keep backups private. Do not
restore a localhost proxy whose listener has been removed.
