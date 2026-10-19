# Usage: .\scripts\new-client.ps1 "Client Name"
param([Parameter(Mandatory=$true)][string]$Name)
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Plain = -join ($Name.Normalize([Text.NormalizationForm]::FormD).ToCharArray() | Where-Object { [Globalization.CharUnicodeInfo]::GetUnicodeCategory($_) -ne 'NonSpacingMark' })
$Slug = ($Plain.ToLower() -replace '[^a-z0-9]+','-').Trim('-')
$Dest = Join-Path $Root "clients\$Slug"
if (Test-Path $Dest) { Write-Error "Already exists: $Dest" }
$Today = Get-Date -Format "dd/MM/yyyy"
Copy-Item -Recurse (Join-Path $Root "clients\_TEMPLATE") $Dest
Get-ChildItem $Dest -Filter *.md | ForEach-Object {
  (Get-Content $_.FullName -Raw).Replace('{{CLIENT_NAME}}',$Name).Replace('{{DATE}}',$Today) | Set-Content $_.FullName -Encoding UTF8
}
Write-Host "Note: open 03-engagement-letter.docx and replace {{CLIENT_NAME}} and {{DATE}} (Ctrl+H)."
Add-Content (Join-Path $Root "office\work-log.md") "$Today | New client folder created: $Name | new-client.ps1"
Write-Host "Created $Dest"
