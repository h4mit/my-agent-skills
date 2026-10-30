# My Agent Skills

Reusable skills and practical notes for repairing desktop networking and managing
Happ and Hiddify on Linux, macOS, and Windows.

| Skill | Use it for |
| --- | --- |
| [os-network-repair](skills/os-network-repair/SKILL.md) | Diagnose connectivity, fix a Happ subscription, and verify automatic connection. |
| [hiddify-uninstall](skills/hiddify-uninstall/SKILL.md) | Remove the actual Hiddify installation while preserving saved profiles. |

Start with [HELP.md](HELP.md) for installation and repeatable prompts on each OS.
Read [TIPS.md](TIPS.md) for the lessons behind these workflows.

These are instruction-only skills. They guide an agent using the tools available
on the current machine; installing them does not change the network or install a
VPN client.

The originating repair was verified on Ubuntu with Happ 4.6.1: importing the
provider's native Hysteria2 subscription resolved a sing-box JSON/Xray mismatch.
Traffic used the selected Germany server, and the login connection launcher was
validated. Windows and macOS instructions have not been run on those platforms.

Subscription URLs, server credentials, profile databases, and machine backups
belong outside this repository. Supply your current subscription privately when
running the skill.
