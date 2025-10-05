# Windows Cleanup Script for pybricks-robos project
# Created: October 5, 2025
# Run this script in PowerShell as Administrator to revert changes made by windows_setup.ps1

# Check if running as administrator
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "This script needs to be run as Administrator. Please restart PowerShell as Administrator." -ForegroundColor Red
    exit 1
}

function Write-ColorMessage {
    param([string]$message)
    Write-Host ">>> $message" -ForegroundColor Magenta
}

Write-ColorMessage "Starting cleanup of changes made by windows_setup.ps1..."

# Remove Python virtual environment
if (Test-Path -Path "venv") {
    Write-ColorMessage "Removing Python virtual environment..."
    Remove-Item -Path "venv" -Recurse -Force
}

# Uninstall global npm packages
if (Get-Command npm -ErrorAction SilentlyContinue) {
    Write-ColorMessage "Uninstalling global npm packages..."
    npm uninstall -g electron-builder electron-vite
}

# Clean node_modules in ui directory
if (Test-Path -Path "ui\node_modules") {
    Write-ColorMessage "Removing UI node_modules..."
    Remove-Item -Path "ui\node_modules" -Recurse -Force
}

# Delete downloaded Zadig tool
$zadigPath = "$env:USERPROFILE\Downloads\zadig-2.8.exe"
if (Test-Path -Path $zadigPath) {
    Write-ColorMessage "Removing downloaded Zadig tool..."
    Remove-Item -Path $zadigPath -Force
}

# Optional: Uninstall Chocolatey packages (uncomment if you want to remove them)
Write-ColorMessage "The following software was installed by the setup script:"
Write-ColorMessage "- Git"
Write-ColorMessage "- Python"
Write-ColorMessage "- Node.js"
Write-Host ""
$uninstallPackages = Read-Host "Do you want to uninstall these programs? (y/n)"

if ($uninstallPackages -eq "y" -or $uninstallPackages -eq "Y") {
    if (Get-Command choco -ErrorAction SilentlyContinue) {
        Write-ColorMessage "Uninstalling Git, Python, and Node.js..."
        choco uninstall -y nodejs python git
    } else {
        Write-ColorMessage "Chocolatey not found. Please uninstall these programs manually from Windows Settings > Apps."
    }
}

# Optional: Uninstall Chocolatey itself
$uninstallChoco = Read-Host "Do you want to uninstall Chocolatey itself? (y/n)"
if ($uninstallChoco -eq "y" -or $uninstallChoco -eq "Y") {
    if (Test-Path -Path "$env:ProgramData\chocolatey") {
        Write-ColorMessage "Uninstalling Chocolatey..."
        Remove-Item -Path "$env:ProgramData\chocolatey" -Recurse -Force
        Write-ColorMessage "Removing Chocolatey from environment variables..."
        $machinePath = [Environment]::GetEnvironmentVariable("PATH", "Machine")
        $machinePathArray = $machinePath -split ";" | Where-Object { $_ -notlike "*chocolatey*" }
        $newMachinePath = $machinePathArray -join ";"
        [Environment]::SetEnvironmentVariable("PATH", $newMachinePath, "Machine")
    }
}

# Reset PowerShell execution policy if desired
$resetPolicy = Read-Host "Do you want to reset PowerShell execution policy to its default (Restricted)? (y/n)"
if ($resetPolicy -eq "y" -or $resetPolicy -eq "Y") {
    Write-ColorMessage "Resetting PowerShell execution policy..."
    Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope CurrentUser -Force
}

Write-ColorMessage "Cleanup completed!"
Write-ColorMessage "Note: Some changes may require manual reversal, and system services that were started may still be running."
Write-ColorMessage "To fully return to the original state, a system restart is recommended."