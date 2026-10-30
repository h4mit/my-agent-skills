# Network repair tips

## Diagnose before changing settings

A connected Wi-Fi interface does not prove internet access. Check the default
route, DNS resolution, a timed HTTPS request, and the affected app separately.
If all checks pass, ask for the failing app/site instead of resetting networking.

GNOME proxy mode `none` disables its saved proxy endpoints. Old values such as
`127.0.0.1:12334` are inactive in that mode; clearing them is cleanup, not proof
of a repaired failure. Check environment variables and browser overrides too.

Docker bridges are not automatically VPN leftovers. Preserve their routes and
check that a new tunnel's address range does not overlap container networks.

## Match the subscription to the engine

Valid JSON can still target the wrong proxy engine. In this repair, the supplied
JSON used sing-box fields such as `inbounds[].type` and `route`; Happ passed it
to Xray, which failed with:

```text
Listen on AnyIP but no Port(s) set in InboundDetour
```

The provider's native response contained four Hysteria2 links. Importing that
response let Happ build compatible configurations and connect successfully.
[Happ documents its Xray JSON passthrough behavior](https://www.happ.su/main/dev-docs/examples-of-links-and-parameters).

Removing `format=json` worked for this provider. It is not a universal conversion:
check the provider's native format, preserve authentication and unrelated query
parameters, and never disable TLS verification to make a subscription download.

After importing, explicitly select a working server from the new subscription.
`happ://connect` can reconnect the previously selected, incompatible entry.
Server IDs, window coordinates, ports, and executable paths vary by installation.

## Verify traffic, not just the UI

An active tunnel or a Connected label is insufficient. Check that a public
destination routes through the tunnel, test several HTTPS sites, and confirm the
expected exit address or country. A country alone cannot identify a specific
provider; compare the expected endpoint or provider information when available.

Use `curl --noproxy '*'` for a controlled test without an application proxy;
it still follows OS tunnel routes. Test application proxy mode with an explicit
proxy separately. Successful DNS resolution does not establish DNS privacy;
inspect how DNS traffic is routed if the user requests it.

## Make startup useful and reversible

Launching Happ and connecting Happ are separate actions. On the verified Linux
installation, an XDG launcher ran the discovered executable with `happ://connect`.
The launcher was validated and invoked successfully. A reboot/login itself was
not tested, so future runs must distinguish launcher tests from login tests.

Automatic connection is not a kill switch, a before-login VPN, or a guarantee
that traffic cannot go direct after a disconnect. Configure those only if asked.
Keep only one intended startup mechanism to avoid duplicate app launches.

A GUI process can legitimately keep running. Do not launch it with a short
`subprocess.run(..., timeout=...)` and accidentally kill it on timeout. Launch it
in the background with private logs and check its status separately.

## Remove the installation that actually exists

An AppImage may live in Documents rather than Applications, with its only
launcher in `~/.local/share/applications`. Follow the launcher's `Exec` path.
Remove the confirmed executable, launcher, and dedicated icons; preserve saved
profiles unless deletion was requested. Package-manager removal is appropriate
only when that package manager owns the installation.

## Keep private material outside Git

Subscription URLs can be credentials. Avoid printing complete downloaded
configs, password fields, profile databases, full browser profiles, or proxy
environment values. Back up locally with restricted access before changes.
Do not commit those backups, raw logs, or live URLs into a skills repository.
