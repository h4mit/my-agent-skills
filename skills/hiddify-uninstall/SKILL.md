---
name: hiddify-uninstall
description: Uninstall Hiddify on Linux, macOS, or Windows by identifying the real installation method, preserving saved profiles by default, and checking networking afterward.
---

# Uninstall Hiddify

Identify the current OS and the actual installation before removing anything.
Use the user's existing authorization for the uninstall; request elevated
execution only through the host's normal permission mechanism when required.

## Find the installation

| OS | Inspect |
| --- | --- |
| Linux | Executable lookup, package ownership, Snap/Flatpak listings when installed, desktop launchers, AppImages, and autostart entries. |
| macOS | The installed application bundle, package-manager ownership, Login Items, and Hiddify's own uninstall instructions for helpers. |
| Windows | Installed apps, installed shortcut targets, package-manager ownership, and Hiddify's registered uninstaller. |

On Linux, inspect `Exec` in launchers under the user's application directory and
system application directories. An AppImage may be in Documents or Downloads.
A failed package query does not prove Hiddify is absent.

Check active Hiddify processes, tunnels, services, proxy mode, proxy listeners,
and startup entries. Distinguish Hiddify from a replacement client such as Happ.
Do not stop another client's engine just because both use Xray or sing-box.

## Remove the confirmed application

1. Disconnect Hiddify through its supported controls and let it release its
   proxy/tunnel settings. Check process ownership before stopping a leftover.
2. Preserve profile databases, subscription files, settings, and credentials
   unless the user explicitly requested a purge. Use private backups if needed.
3. Use the owning package manager or registered uninstaller for a managed
   installation. On macOS, follow the app's supported helper-removal procedure.
4. For a portable AppImage, remove only its confirmed executable, launcher,
   dedicated icons, and Hiddify-specific startup entry. Validate exact paths
   before removal; avoid wildcard deletion and recursive home-directory cleanup.
5. Refresh desktop/icon caches when the relevant platform tools are available.

For the originating Linux AppImage installation, saved data lived under
`~/.local/share/hiddify`; that is an observation, not a universal purge path.
Do not publish or read out its profile database or downloaded subscriptions.

## Check networking afterward

Verify that the executable/launcher is gone, Hiddify is no longer running, and
its startup entry or service is removed when applicable. An application data
directory remaining is consistent with preserving profiles.

Inspect active proxy settings before changing them. An inactive saved endpoint
does not explain a network failure. Reset only an orphaned endpoint proven to
belong to Hiddify, keeping unrelated proxy/PAC settings and replacement clients.

Test DNS resolution, the internet route, and timed HTTPS access after removal.
If a replacement VPN is intentionally active, verify its route rather than
forcing traffic direct. Preserve Docker bridges and unrelated network services.

Report the removed installation and artifacts, preserved data, connectivity
results, and any leftover that requires additional authorization. Do not report
complete removal if required uninstall steps or verification failed.
