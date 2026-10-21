$ErrorActionPreference = 'Stop'
$platformRoot = Split-Path $PSScriptRoot -Parent
$repoRoot = Join-Path $platformRoot 'repos'
New-Item -ItemType Directory -Force $repoRoot | Out-Null
foreach ($name in @('extract','ingest','documents','web')) {
    $destination = Join-Path $repoRoot "dds-pdf-$name"
    if (!(Test-Path -LiteralPath $destination)) {
        git clone "https://github.com/TomiCaratti13/dds-pdf-$name.git" $destination
        if ($LASTEXITCODE -ne 0) { throw "No se pudo clonar $name" }
    } else { Write-Output "Existe $destination; se conserva su estado local." }
}
