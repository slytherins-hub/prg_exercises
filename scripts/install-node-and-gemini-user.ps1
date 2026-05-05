# install-node-and-gemini-user.ps1
# Nainstaluje pevně danou Node.js LTS verzi do %LOCALAPPDATA%\nodejs bez admin práv,
# přidá ji do User PATH a hned doinstaluje Gemini CLI (@google/gemini-cli) globálně.
#
# Spuštění (PowerShell):
#   irm https://gist.githubusercontent.com/tomasvicar/00b7135377088268667fbcd5f04dea14/raw/install-node-and-gemini-user.ps1 | iex
#
# Po dokončení otevři NOVÝ terminál a spusť:
#   gemini

$ErrorActionPreference = 'Stop'

$ver = 'v24.15.0'
$dest = Join-Path $env:LOCALAPPDATA 'nodejs'

$zipName = "node-$ver-win-x64.zip"
$folderName = "node-$ver-win-x64"
$zipPath = Join-Path $env:TEMP $zipName
$url = "https://nodejs.org/dist/$ver/$zipName"

Write-Host "Instaluji Node.js $ver"
Write-Host "Stahuji $url ..."
Invoke-WebRequest -Uri $url -OutFile $zipPath

if (Test-Path $dest) {
    Write-Host "Mažu starou instalaci v $dest ..."
    Remove-Item $dest -Recurse -Force
}

$extractRoot = $env:LOCALAPPDATA
$extractedFolder = Join-Path $extractRoot $folderName

if (Test-Path $extractedFolder) {
    Remove-Item $extractedFolder -Recurse -Force
}

Write-Host "Rozbaluji do $extractRoot ..."
Expand-Archive -Path $zipPath -DestinationPath $extractRoot -Force

Rename-Item -Path $extractedFolder -NewName 'nodejs'

$userPath = [Environment]::GetEnvironmentVariable('Path', 'User')

if ([string]::IsNullOrWhiteSpace($userPath)) {
    $newUserPath = $dest
}
elseif ($userPath -notlike "*$dest*") {
    $newUserPath = "$userPath;$dest"
}
else {
    $newUserPath = $userPath
}

[Environment]::SetEnvironmentVariable('Path', $newUserPath, 'User')

Remove-Item $zipPath -Force

# Přidání Node do PATH aktuálního procesu, aby šel hned spustit npm bez restartu terminálu
$env:Path = "$dest;$env:Path"

Write-Host ""
Write-Host "Node.js $ver nainstalován v $dest" -ForegroundColor Green
Write-Host "Instaluji Gemini CLI (@google/gemini-cli) ..." -ForegroundColor Cyan

$npmCmd = Join-Path $dest 'npm.cmd'
& $npmCmd install -g '@google/gemini-cli'

if ($LASTEXITCODE -ne 0) {
    throw "Instalace Gemini CLI selhala (npm exit code $LASTEXITCODE)."
}

Write-Host ""
Write-Host "==============================================" -ForegroundColor Green
Write-Host " Hotovo! Node.js $ver + Gemini CLI nainstalovány." -ForegroundColor Green
Write-Host " Otevři NOVÝ terminál a spusť:" -ForegroundColor Green
Write-Host "   gemini" -ForegroundColor Yellow
Write-Host " Při prvním spuštění zvol 'Sign in with Google'." -ForegroundColor Green
Write-Host "==============================================" -ForegroundColor Green
