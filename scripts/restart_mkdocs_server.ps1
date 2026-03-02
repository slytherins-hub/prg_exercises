param(
    [string]$BindHost = "127.0.0.1",
    [int]$Port = 8000,
    [switch]$NoBuild,
    [switch]$Foreground,
    [switch]$StopOnly
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Path $PSScriptRoot -Parent
$tmpDir = Join-Path $repoRoot ".tmp"
$pidFile = Join-Path $tmpDir "mkdocs-serve-$Port.pid"
$logFile = Join-Path $tmpDir "mkdocs-serve-$Port.log"
$errFile = Join-Path $tmpDir "mkdocs-serve-$Port.err.log"
$bindAddress = "{0}:{1}" -f $BindHost, $Port
$url = "http://$bindAddress/"

if (-not (Test-Path $tmpDir)) {
    New-Item -ItemType Directory -Path $tmpDir | Out-Null
}

function Stop-ProcessIfRunning {
    param([int]$ProcessId)

    if ($ProcessId -le 0) {
        return
    }

    $proc = Get-Process -Id $ProcessId -ErrorAction SilentlyContinue
    if ($null -ne $proc) {
        Write-Host "Stopping process PID=$ProcessId ($($proc.ProcessName))"
        try {
            & taskkill /PID $ProcessId /T /F *> $null
        }
        catch {
        }
        if ($LASTEXITCODE -ne 0) {
            Stop-Process -Id $ProcessId -Force -ErrorAction SilentlyContinue
        }
        Start-Sleep -Milliseconds 300
    }
}

function Stop-MkDocsFromPidFile {
    if (-not (Test-Path $pidFile)) {
        return
    }

    $raw = Get-Content -Path $pidFile -ErrorAction SilentlyContinue | Select-Object -First 1
    $pidFromFile = 0
    if ([int]::TryParse($raw, [ref]$pidFromFile)) {
        Stop-ProcessIfRunning -ProcessId $pidFromFile
    }

    Remove-Item -Path $pidFile -Force -ErrorAction SilentlyContinue
}

function Stop-MkDocsByCommandLine {
    $pattern = [regex]::Escape("mkdocs serve -a $bindAddress")
    $procs = Get-CimInstance Win32_Process | Where-Object {
        $_.CommandLine -and ($_.CommandLine -match $pattern)
    }

    foreach ($proc in $procs) {
        Stop-ProcessIfRunning -ProcessId $proc.ProcessId
    }
}

function Free-Port {
    $listeners = Get-NetTCPConnection -State Listen -LocalPort $Port -ErrorAction SilentlyContinue
    foreach ($listener in $listeners) {
        Stop-ProcessIfRunning -ProcessId $listener.OwningProcess
    }
}

function Wait-ForServer {
    param([int]$TimeoutSeconds = 20)

    $deadline = (Get-Date).AddSeconds($TimeoutSeconds)
    while ((Get-Date) -lt $deadline) {
        try {
            $response = Invoke-WebRequest -Uri $url -UseBasicParsing -TimeoutSec 2
            if ($response.StatusCode -ge 200 -and $response.StatusCode -lt 500) {
                return $true
            }
        }
        catch {
        }
        Start-Sleep -Milliseconds 500
    }

    return $false
}

Write-Host "Preparing MkDocs server restart on $bindAddress"

Stop-MkDocsFromPidFile
Stop-MkDocsByCommandLine
Free-Port

if ($StopOnly) {
    Write-Host "Server stop-only mode completed."
    exit 0
}

if (-not $NoBuild) {
    Write-Host "Running build: uv run mkdocs build"
    Push-Location $repoRoot
    try {
        uv run mkdocs build
        if ($LASTEXITCODE -ne 0) {
            throw "mkdocs build failed"
        }
    }
    finally {
        Pop-Location
    }
}

if ($Foreground) {
    Write-Host "Starting server in foreground: uv run mkdocs serve -a $bindAddress"
    Push-Location $repoRoot
    try {
        uv run mkdocs serve -a $bindAddress
    }
    finally {
        Pop-Location
    }
    exit $LASTEXITCODE
}

Write-Host "Starting server in background..."
if (Test-Path $logFile) { Remove-Item $logFile -Force -ErrorAction SilentlyContinue }
if (Test-Path $errFile) { Remove-Item $errFile -Force -ErrorAction SilentlyContinue }

$serverProcess = Start-Process -FilePath "uv" `
    -ArgumentList @("run", "mkdocs", "serve", "-a", $bindAddress) `
    -WorkingDirectory $repoRoot `
    -WindowStyle Hidden `
    -RedirectStandardOutput $logFile `
    -RedirectStandardError $errFile `
    -PassThru

Set-Content -Path $pidFile -Value $serverProcess.Id -Encoding ascii

if (Wait-ForServer -TimeoutSeconds 20) {
    Write-Host "MkDocs server is up: $url"
    Write-Host "PID: $($serverProcess.Id)"
    Write-Host "Server runs hidden in background."
    Write-Host "Logs: $logFile"
    exit 0
}

Write-Host "Server did not become healthy in time. Stopping PID $($serverProcess.Id)."
Stop-ProcessIfRunning -ProcessId $serverProcess.Id

Write-Host "--- stdout (last lines) ---"
if (Test-Path $logFile) {
    Get-Content -Path $logFile -Tail 40
}

Write-Host "--- stderr (last lines) ---"
if (Test-Path $errFile) {
    Get-Content -Path $errFile -Tail 40
}

exit 1
