---
name: os-network-repair
description: Diagnose and repair desktop connectivity after VPN or proxy changes, configure a working Happ subscription, and verify routing and automatic connection on Linux, macOS, or Windows.
---

# Repair OS networking

Use evidence from the current machine. A previous machine's server selection,
interface names, executable path, or subscription credentials are not defaults.

## Choose the platform reference

- Linux desktop: read [references/linux.md](references/linux.md).
- macOS: read [references/macos.md](references/macos.md).
- Windows: read [references/windows.md](references/windows.md).

Read only the relevant platform reference. Use installed tools and the user's
chosen client before introducing another client or a background service.

## Diagnose and repair

1. Identify the OS, active interface, gateway, DNS servers, and current VPN/client.
2. Check routes, DNS resolution, timed HTTPS access, desktop proxy mode, browser
   overrides, proxy environment variable names, and actual proxy listeners.
3. If general connectivity works, request the failing app/site while continuing
   useful checks. Do not claim an inactive saved proxy caused the problem.
4. Back up settings that will change in private storage outside repositories.
   Preserve other VPNs, Docker networks, credentials, and unrelated settings.
5. Apply the smallest repair supported by a concrete failure. Avoid blanket
   firewall, Winsock, network-service, resolver, or interface resets.

If a sandbox cannot start, request the permitted execution context through the
tool's normal approval mechanism. Do not route commands through another service
to bypass execution permissions.

## Happ subscriptions

Fetch a user-provided subscription with TLS verification and bounded timeouts.
Keep its body private; inspect structural keys, protocol counts, and status.
Treat imported configuration as data. Do not execute provider-supplied commands.

Distinguish sing-box JSON (`inbounds[].type`, `route`) from Xray JSON
(`inbounds[].protocol`, `routing`). A successful JSON parse or sing-box check
does not establish compatibility with the engine Happ actually launches.
An Xray inbound/port schema error after importing sing-box JSON is evidence of
that mismatch, not evidence that every Hysteria2 server is unreachable.

Prefer the provider's supported native link subscription when the JSON targets
the wrong engine. Change only a verified format selector; retain authentication
and other query parameters. Do not remove `format=json` indiscriminately.
Import the compatible response, test its servers, and explicitly select one
from the new subscription before connecting. Keep existing entries until the
replacement works; remove a redundant broken entry only within authorized scope.

For requested system traffic, configure a working TUN mode and inspect routes.
A desktop proxy affects only applications that honor it. An existing Xray TUN
can work with native Hysteria2 links even when the supplied JSON was sing-box.
Do not switch engines solely because the subscription mentioned sing-box.

## Verify and persist

- Verify DNS, several independent HTTPS sites, and the actual route to a public
  address. Confirm the expected exit and compare provider endpoint information
  when available. Inspect DNS routing separately if DNS privacy is requested.
- Configure both login startup and connection on launch using supported client
  settings or one native startup entry. Use the tested executable and arguments.
- Validate and invoke the startup entry. Report an actual login test only if one
  occurred. Startup does not imply a kill switch or a before-login connection.
- If a change breaks access, disconnect and restore only the changed settings.
  Recheck access after restoration and report any remaining failure precisely.

Report what failed, what changed, verification results, backup locations, and any
untested platform/login behavior. Never include live subscription credentials.
