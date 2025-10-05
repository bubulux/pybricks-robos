# Windows 11 Setup Script for pybricks-robos project
# Created: October 5, 2025
# Run this script in PowerShell as Administrator

# Check if running as administrator
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "This script needs to be run as Administrator. Please restart PowerShell as Administrator." -ForegroundColor Red
    exit 1
}

function Write-ColorMessage {
    param([string]$message)
    Write-Host ">>> $message" -ForegroundColor Cyan
}

# Set execution policy to allow script execution
Write-ColorMessage "Setting PowerShell execution policy..."
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force

# Install Chocolatey if not installed
if (-not (Get-Command choco -ErrorAction SilentlyContinue)) {
    Write-ColorMessage "Installing Chocolatey package manager..."
    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
    Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    # Refresh environment variables
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
} else {
    Write-ColorMessage "Chocolatey is already installed."
}

# Install required packages using Chocolatey
Write-ColorMessage "Installing system dependencies using Chocolatey..."
choco install -y git python nodejs

# Check if Python is installed
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python installation failed. Please install Python 3 manually." -ForegroundColor Red
    exit 1
}

# Check versions
$pythonVersion = (python --version) | Out-String
$nodeVersion = (node -v) | Out-String
$npmVersion = (npm -v) | Out-String
Write-ColorMessage "Python version: $pythonVersion"
Write-ColorMessage "Node.js version: $nodeVersion"
Write-ColorMessage "npm version: $npmVersion"

# Set up Python virtual environment
Write-ColorMessage "Setting up Python virtual environment..."
if (-not (Test-Path -Path "venv")) {
    python -m venv venv
    Write-ColorMessage "Virtual environment created."
} else {
    Write-ColorMessage "Virtual environment already exists."
}

# Activate the virtual environment and install Python dependencies
Write-ColorMessage "Installing Python dependencies..."
& .\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install wheel
python -m pip install -r requirements.txt

# Install global npm packages
Write-ColorMessage "Installing global npm packages..."
npm install -g electron-builder electron-vite

# Install UI dependencies
if (Test-Path -Path "ui") {
    Write-ColorMessage "Installing UI dependencies..."
    Push-Location ui
    npm install
    Pop-Location
} else {
    Write-ColorMessage "Warning: UI directory not found." -ForegroundColor Yellow
}

# Install Zadig for USB driver installation (helpful for LEGO USB devices)
Write-ColorMessage "Downloading Zadig for USB driver installation..."
$zadigUrl = "https://github.com/pbatard/libwdi/releases/download/v1.5.0/zadig-2.8.exe"
$zadigPath = "$env:USERPROFILE\Downloads\zadig-2.8.exe"
(New-Object System.Net.WebClient).DownloadFile($zadigUrl, $zadigPath)

# Install Bluetooth drivers and enable Bluetooth services
Write-ColorMessage "Ensuring Bluetooth services are running..."
Get-Service -Name "BTAGService", "bthserv" | Start-Service
Get-Service -Name "BTAGService", "bthserv" | Set-Service -StartupType Automatic

Write-ColorMessage "Installation complete!"
Write-ColorMessage "To use the Python environment, run: .\venv\Scripts\Activate.ps1"
Write-ColorMessage "To run the UI in development mode, go to the ui directory and run: npm run dev"
Write-ColorMessage "If you need to install USB drivers for LEGO devices, run Zadig from: $zadigPath"
Write-ColorMessage "Remember to pair your Bluetooth devices in Windows Settings > Bluetooth & devices"