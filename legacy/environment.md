# Environment Setup Guide

This document outlines the steps taken to install Node.js and configure the environment PATH on Windows using Bash.

## Prerequisites
- Windows 10/11
- Git Bash or similar Bash shell
- Windows Package Manager (winget) - comes with Windows 10/11

## Step-by-Step Installation Process

### 1. Check if Node.js is already installed
```bash
node --version
npm --version
```
*Expected result: "command not found" if not installed*

### 2. Verify winget is available
```bash
winget --version
```
*Expected result: Version number (e.g., v1.11.430)*

### 3. Install Node.js using winget
```bash
winget install OpenJS.NodeJS
```
*This installs Node.js LTS version (v24.8.0 at time of setup)*

### 4. Check current PATH (optional - for debugging)
```bash
echo $PATH
```
*This shows current PATH without Node.js*

### 5. Verify Node.js installation location
```bash
ls "/c/Program Files/nodejs"
```
*Expected result: Shows node.exe, npm, npm.cmd, etc.*

### 6. Temporarily add Node.js to PATH for current session
```bash
export PATH="/c/Program Files/nodejs:$PATH"
```

### 7. Test temporary PATH update
```bash
node --version
npm --version
```
*Expected result: v24.8.0 and 10.2.5 respectively*

### 8. Make PATH changes permanent - Add to .bashrc
```bash
echo 'export PATH="/c/Program Files/nodejs:$PATH"' >> ~/.bashrc
```

### 9. Reload bash profile to apply changes
```bash
source ~/.bashrc
```

### 10. Verify permanent installation
```bash
node --version
npm --version
```
*Should work in new terminal sessions*

## Final Verification

Open a new terminal and run:
```bash
node --version
npm --version
```

Both commands should return version numbers without any additional PATH exports.

## Notes

- The installation placed Node.js in: `C:\Program Files\nodejs\`
- npm (Node Package Manager) was included automatically
- npx (Node Package Runner) was also installed
- The PATH modification affects only Bash shells (Git Bash, WSL, etc.)
- For system-wide PATH changes, use Windows Environment Variables GUI

## Troubleshooting

If Node.js is not found after following these steps:

1. Check if the path exists: `ls "/c/Program Files/nodejs"`
2. Verify .bashrc content: `cat ~/.bashrc | grep nodejs`
3. Reload profile: `source ~/.bashrc`
4. Try opening a new terminal window

## Alternative Installation Methods

### Using Official Installer
1. Download from https://nodejs.org/
2. Run the .msi installer
3. Follow setup wizard
4. Restart terminal

### Using Chocolatey (if installed)
```bash
choco install nodejs
```

### Using Scoop (if installed)
```bash
scoop install nodejs
```