# Linux desktop networking and Happ

## Inspect without changing the connection

Discover available commands and substitute the actual interface/client paths.

```sh
cat /etc/os-release
nmcli -t -f DEVICE,TYPE,STATE,CONNECTION device status
ip -brief address
ip route
ip rule show
resolvectl status
getent ahostsv4 example.com
gsettings get org.gnome.system.proxy mode
ss -lntp
curl --noproxy '*' -I --connect-timeout 5 --max-time 12 https://example.com
```

NetworkManager, systemd-resolved, and GNOME commands apply only when those
components are installed. On other desktops, inspect their actual proxy and
resolver configuration. Review environment variable names without printing
credential-bearing values. Check browser proxy flags without dumping all args.

Before proxy edits on GNOME, save `dconf dump /system/proxy/` to a private backup.
Mode `none` means stored hosts/ports are inactive. Clear only confirmed obsolete
endpoints when appropriate; preserve unrelated bypass, PAC, and authentication
settings. Flush DNS only when useful, and do not replace `/etc/resolv.conf` with
an arbitrary static file.

Inspect `ip route get 1.1.1.1`, tunnel address ranges, and Docker routes. Do not
delete container bridges to repair an unrelated VPN failure.

## Find Happ and back up settings

Find the package's launcher and inspect its `Exec` field. On the verified Ubuntu
installation the executable was `/opt/happ/bin/Happ`, its daemon was
`happd.service`, and its bundled engines included Xray and sing-box. Discover
these paths again; do not install a second daemon or assume passwordless sudo.

Private backups may include `~/.config/Happ.conf` and
`~/.config/Happ/subs.db` when present. Use SQLite's backup API for a live database.
Do not modify an opaque profile database to guess its schema or server IDs.
Do not edit running-client settings that may be overwritten on exit.

## Import and connect

Use Happ's supported import UI or the locally supported `happ://add/` deep link
with the compatible native subscription. Keep the URL out of public logs and
startup entries. Discover the UI controls again; saved screen coordinates from
another session are unreliable.

After selecting a tested server, the verified Linux executable accepts:

```sh
/opt/happ/bin/Happ happ://connect
```

Substitute the discovered path. A new GUI process may remain running; launch it
in the background with private logs instead of killing it with a short timeout.
When an instance already runs, check that the deep link reached that instance.
Monitor the client result and actual tunnel/route after issuing the command.

## Connect at login

Prefer the app's working startup and auto-connect controls. Otherwise use one
XDG entry in `${XDG_CONFIG_HOME:-$HOME/.config}/autostart/happ-proxy.desktop`.
Back up an existing entry before replacing it. Substitute the executable below;
quote paths containing spaces according to the desktop-entry specification.

```ini
[Desktop Entry]
Type=Application
Name=Happ Proxy
Exec=/opt/happ/bin/Happ happ://connect
Icon=happ
Terminal=false
StartupNotify=false
X-GNOME-Autostart-enabled=true
```

Validate and exercise the actual entry when the tools are available:

```sh
desktop-file-validate "$HOME/.config/autostart/happ-proxy.desktop"
gio launch "$HOME/.config/autostart/happ-proxy.desktop"
ip route get 1.1.1.1
curl --noproxy '*' -I --connect-timeout 5 --max-time 12 https://www.google.com
curl --noproxy '*' --fail --connect-timeout 5 --max-time 10 https://ipinfo.io/country
```

Use the actual XDG path for both commands if it differs from the example. The
route should use the intended tunnel and the exit should match the selected
server. Repeat DNS and another site's HTTPS test; check DNS routing separately
when needed. A launcher test does not test a future login.

For rollback, disconnect Happ, remove only the entry created for this repair,
and restore backed-up settings if necessary. Verify direct access afterward.

The [XDG autostart specification](https://specifications.freedesktop.org/autostart/latest/)
defines startup after desktop login; it is not a system boot VPN service.
