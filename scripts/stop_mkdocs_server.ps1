param(
    [int]$Port = 8000,
    [string]$BindHost = "127.0.0.1"
)

$ErrorActionPreference = "Stop"

$restartScript = Join-Path $PSScriptRoot "restart_mkdocs_server.ps1"
if (-not (Test-Path $restartScript)) {
    throw "Missing script: $restartScript"
}

powershell -ExecutionPolicy Bypass -File $restartScript -BindHost $BindHost -Port $Port -StopOnly
