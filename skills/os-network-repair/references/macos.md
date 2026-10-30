# macOS networking and Happ

These instructions are a platform reference. The originating repair was verified
on Ubuntu, not macOS. Discover the installed app and current network service.

## Diagnose

```sh
sw_vers
networksetup -listallnetworkservices
route -n get default
scutil --dns
scutil --proxy
dscacheutil -q host -a name example.com
curl --noproxy '*' -I --connect-timeout 5 --max-time 12 https://example.com
```

Inspect the actual active service's HTTP, HTTPS, SOCKS, and automatic proxy
settings before changing them. Save the current settings privately. Do not
assume the service is named Wi-Fi or clear an unrelated corporate PAC profile.
Test the affected app separately when DNS and general HTTPS work.

## Connect Happ

Find the installed Happ application and its version. Back up its settings using
the app's supported export or the discovered local storage. Choose the existing
client and its documented controls instead of guessing a Linux filesystem path.

Import the provider's supported native subscription if its JSON was built for a
different engine. Preserve authentication and other URL parameters. Select and
test a server from the compatible subscription before connecting.

For system traffic, enable a supported TUN/VPN mode and complete any macOS
extension or administrator approval through the normal UI. Do not disable
system security protections. A system HTTP proxy alone does not cover all apps.

If the installed app registers `happ://`, test its connect URL:

```sh
open 'happ://connect'
```

If URL handling is absent or does not connect the selected server, use the app's
controls; do not assume the command worked because `open` exited successfully.

## Persist and verify

Enable Happ's supported connection-on-launch setting and test it. Then add Happ
under System Settings > General > Login Items, using the label shown by that
macOS release. Starting the app alone does not establish automatic connection.
See [Apple's Login Items guide](https://support.apple.com/en-ie/guide/mac-help/mh15189/27/mac/27).

```sh
route -n get 1.1.1.1
scutil --dns
curl --noproxy '*' -I --connect-timeout 5 --max-time 12 https://www.google.com
curl --noproxy '*' -I --connect-timeout 5 --max-time 12 https://github.com
curl --noproxy '*' --fail --connect-timeout 5 --max-time 10 https://ipinfo.io/country
```

Confirm that the intended tunnel handles internet traffic and the exit matches
the selected server. Verify any requested DNS routing separately. Record whether
connection-on-launch and a real login were tested.

For rollback, disconnect Happ, remove only the newly added login item, and restore
the changed proxy/DNS settings. Preserve unrelated VPNs and network extensions.
