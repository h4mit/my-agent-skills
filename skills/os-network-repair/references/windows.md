# Windows networking and Happ

These instructions are a platform reference. The originating repair was verified
on Ubuntu, not Windows. Use PowerShell; discover the installed Happ executable.

## Diagnose

```powershell
Get-NetIPConfiguration
Get-NetRoute -DestinationPrefix '0.0.0.0/0'
Get-DnsClientServerAddress
Resolve-DnsName example.com
netsh winhttp show proxy
Get-ChildItem Env:*proxy* | Select-Object Name
curl.exe --noproxy '*' -I --connect-timeout 5 --max-time 12 https://example.com
```

Inspect Settings > Network & internet > Proxy, the affected browser's overrides,
and actual local listeners. WinHTTP proxy state differs from user/browser proxy
state. Inspect `HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings`
locally if needed, without publishing credential-bearing PAC/proxy values.
Back up only settings that will change. Do not start with a blanket Winsock,
firewall, adapter, or registry reset.

## Connect Happ

Find the installed app's executable, version, and service. A running process can
provide the path through `Get-Process Happ | Select-Object -ExpandProperty Path`.
If absent, use the installed shortcut's target or the app's installation record.
Do not hardcode a Linux path or guess a registry uninstall command.

Back up profiles using supported export or the discovered storage. Import the
provider's native link subscription when the JSON targets a different engine.
Keep authentication parameters intact and explicitly select a tested server from
the new subscription. Use a supported TUN mode for system traffic and complete
required service/administrator approval normally.

If the installed app registers the URL scheme, test:

```powershell
Start-Process 'happ://connect'
```

Otherwise use the discovered executable with `happ://connect` only after
confirming the installed version accepts it. Verify the connection result in
Happ and the OS; a successful process launch is not a successful tunnel.

## Connect at login

Prefer Happ's supported startup and connection-on-launch settings. If necessary,
create one shortcut in the current user's Startup folder, with the discovered
Happ executable as Target and the tested `happ://connect` argument. Do not put the
subscription URL in the shortcut. Preserve any existing shortcut before editing.

Open the per-user Startup folder with:

```powershell
Start-Process explorer.exe 'shell:startup'
```

See [Microsoft's startup application guide](https://support.microsoft.com/en-gb/windows/experience/startup-boot/configure-startup-applications-in-windows).
An app that requires elevation may not connect from an ordinary Startup shortcut;
test the app's service-backed startup before choosing another mechanism. Do not
disable UAC or silently add a highest-privilege scheduled task.

## Verify and undo

```powershell
Find-NetRoute -RemoteIPAddress 1.1.1.1
Resolve-DnsName example.com
curl.exe --noproxy '*' -I --connect-timeout 5 --max-time 12 https://www.google.com
curl.exe --noproxy '*' -I --connect-timeout 5 --max-time 12 https://github.com
curl.exe --noproxy '*' --fail --connect-timeout 5 --max-time 10 https://ipinfo.io/country
```

Check that the actual route uses the intended tunnel and the exit matches the
selected server. Inspect DNS routing separately if requested. Test the shortcut
and report whether a real login was tested.

For rollback, disconnect Happ, remove only the new Startup shortcut, and restore
the settings changed by this repair. Verify normal access again.
