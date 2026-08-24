<#
.SYNOPSIS
  Automatic Graphify & Memory Sync Hook for Git
.DESCRIPTION
  Runs incremental Graphify updates after commits or merges to keep the knowledge graph and mistake memory in sync.
#>

if (Get-Command graphify -ErrorAction SilentlyContinue) {
    Write-Host "[AI-Native SDLC] Updating Graphify knowledge graph and mistake memory..." -ForegroundColor Cyan
    graphify --update
} else {
    Write-Host "[AI-Native SDLC] graphify CLI not found in PATH, skipping automatic sync." -ForegroundColor Yellow
}
