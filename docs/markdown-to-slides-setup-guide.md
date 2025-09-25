# Markdown to Slides Setup Guide
## Complete Implementation Documentation for GCP Certification Prep Project

**Created**: 2024.09.24
**Purpose**: Reproducible setup guide for markdown-to-slides conversion approaches
**Target**: Developers wanting to implement multiple conversion strategies for presentation automation

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Final Directory Structure](#final-directory-structure)
4. [Step-by-Step Implementation](#step-by-step-implementation)
5. [Complete File Contents](#complete-file-contents)
6. [Verification Steps](#verification-steps)
7. [Usage Examples](#usage-examples)
8. [Troubleshooting](#troubleshooting)

---

## Project Overview

This implementation creates a comprehensive testing environment for multiple markdown-to-slides conversion approaches. The goal is to compare different frameworks and methodologies for converting markdown presentations into PPTX files compatible with Google Slides.

### Technologies Implemented

- **Marp CLI**: Node.js-based converter (9.6k GitHub stars)
- **Pandoc Universal**: Universal document converter (39.2k GitHub stars)
- **md2pptx Python**: Custom Python solution using python-pptx library
- **Shared Resources**: Common test content and templates

### Key Features

- ✅ Isolated environments with virtual environments for Python projects
- ✅ Node.js package management for JavaScript-based tools
- ✅ Automated setup script for all approaches
- ✅ Common test content using real GCP certification materials
- ✅ Git ignore configuration excluding all build artifacts
- ✅ Comprehensive documentation for each approach

---

## Prerequisites

### Required Software

```bash
# System Requirements
- Python 3.8+ (for Python-based converters)
- Node.js 16+ (for Marp CLI and Slidev)
- npm (Node Package Manager)
- git (Version control)

# Optional but Recommended
- Pandoc system installation (for Pandoc Universal)
- Docker (for advanced AI integration - future)
```

### Installation Commands

**Ubuntu/Debian:**
```bash
# Update system
sudo apt update

# Install Python 3.8+
sudo apt install python3 python3-pip python3-venv

# Install Node.js 18.x
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install Pandoc (optional but recommended)
sudo apt install pandoc

# Verify installations
python3 --version  # Should be 3.8+
node --version     # Should be 16+
npm --version      # Should be 8+
pandoc --version   # Should show version info
```

**macOS:**
```bash
# Using Homebrew
brew install python@3.11 node pandoc

# Verify installations
python3 --version
node --version
npm --version
pandoc --version
```

---

## Final Directory Structure

The implementation creates the following structure:

```
gcp-pca-certification-prep/
├── .gitignore                 # Git ignore with virtual environment exclusions
├── README.md                  # Project overview
├── rnd/                       # Research documents (existing)
├── apps/                      # Conversion approach implementations
│   ├── 01-marp-cli/          # Marp CLI - Simplest approach
│   │   ├── package.json      # Node.js dependencies
│   │   ├── node_modules/     # Node.js packages (git ignored)
│   │   ├── README.md         # Marp CLI documentation
│   │   ├── scripts/
│   │   │   └── convert.sh    # Conversion script
│   │   ├── output/           # Generated PPTX files
│   │   ├── input/            # Local test files
│   │   ├── config/           # Themes and configurations
│   │   └── examples/         # Sample outputs
│   │
│   ├── 03-md2pptx-python/    # Python PPTX generator
│   │   ├── .venv/            # Virtual environment (git ignored)
│   │   ├── requirements.txt  # Python dependencies
│   │   ├── README.md         # Python implementation docs
│   │   ├── scripts/
│   │   │   └── convert.py    # Python conversion script
│   │   └── [standard subdirs]
│   │
│   ├── 04-pandoc-universal/  # Pandoc-based converter
│   │   ├── .venv/            # Virtual environment (git ignored)
│   │   ├── requirements.txt  # Python dependencies
│   │   ├── README.md         # Pandoc implementation docs
│   │   ├── scripts/
│   │   │   ├── convert.py    # Python wrapper script
│   │   │   └── convert.sh    # Bash conversion script
│   │   └── [standard subdirs]
│   │
│   ├── shared/               # Common resources
│   │   ├── input/            # Test markdown files
│   │   │   └── gcp-cert-prep-slides-v2.md
│   │   ├── templates/        # Shared themes/templates
│   │   └── README.md         # Shared resources docs
│   │
│   ├── setup-all.sh          # Automated setup script
│   └── README.md             # Apps overview and comparison
│
├── docs/                     # Project documentation
│   └── markdown-to-slides-setup-guide.md  # This document
│
└── [other project files]
```

---

## Step-by-Step Implementation

This section documents the exact commands and process used to create the structure above.

### Step 1: Git Configuration

**Purpose**: Configure git to ignore virtual environments and build artifacts

**Commands**:
```bash
# Create root .gitignore file
touch .gitignore
```

**File Content**: [See Complete File Contents section for full .gitignore]

### Step 2: Directory Structure Creation

**Purpose**: Create the directory hierarchy for all conversion approaches

**Commands**:
```bash
# Create all conversion approach directories
mkdir -p apps/{01-marp-cli,02-slidev,03-md2pptx-python,04-pandoc-universal,05-python-pptx-custom,06-presenton-ai}

# Create shared resources directory
mkdir -p apps/shared/{input,templates}

# Verify structure
ls -la apps/
```

**Expected Output**:
```
drwxrwxr-x 9 user user 4096 Sep 24 22:10 .
drwxrwxr-x 6 user user 4096 Sep 24 22:10 ..
drwxrwxr-x 2 user user 4096 Sep 24 22:10 01-marp-cli
drwxrwxr-x 2 user user 4096 Sep 24 22:10 02-slidev
drwxrwxr-x 2 user user 4096 Sep 24 22:10 03-md2pptx-python
drwxrwxr-x 2 user user 4096 Sep 24 22:10 04-pandoc-universal
drwxrwxr-x 2 user user 4096 Sep 24 22:10 05-python-pptx-custom
drwxrwxr-x 2 user user 4096 Sep 24 22:10 06-presenton-ai
drwxrwxr-x 4 user user 4096 Sep 24 22:10 shared
```

### Step 3: Shared Resources Setup

**Purpose**: Create common test content and documentation

**Commands**:
```bash
# Copy GCP test content to shared input
cp rnd/gcp-cert-prep-slides-v2.md apps/shared/input/

# Create shared resources documentation
touch apps/shared/README.md
```

### Step 4: Marp CLI Project Setup

**Purpose**: Set up the simplest conversion approach using Marp CLI

**Commands**:
```bash
cd apps/01-marp-cli

# Initialize Node.js project
npm init -y

# Install Marp CLI
npm install @marp-team/marp-cli

# Create project subdirectories
mkdir -p output input scripts config examples

# Create documentation and scripts
touch README.md scripts/convert.sh

# Make scripts executable
chmod +x scripts/convert.sh

cd ../..
```

### Step 5: md2pptx Python Project Setup

**Purpose**: Set up Python-based PPTX generation with virtual environment

**Commands**:
```bash
cd apps/03-md2pptx-python

# Create virtual environment
python3 -m venv .venv

# Create project structure
mkdir -p output input scripts config examples

# Create requirements file
touch requirements.txt

# Create Python conversion script
touch scripts/convert.py
chmod +x scripts/convert.py

# Create documentation
touch README.md

cd ../..
```

### Step 6: Pandoc Universal Project Setup

**Purpose**: Set up the most flexible converter with both Python and Bash scripts

**Commands**:
```bash
cd apps/04-pandoc-universal

# Create virtual environment
python3 -m venv .venv

# Create project structure
mkdir -p output input scripts config examples

# Create requirements file
touch requirements.txt

# Create conversion scripts (both Python and Bash)
touch scripts/convert.py scripts/convert.sh
chmod +x scripts/convert.py scripts/convert.sh

# Create documentation
touch README.md

cd ../..
```

### Step 7: Automation Script Creation

**Purpose**: Create automated setup script for all approaches

**Commands**:
```bash
cd apps

# Create setup script
touch setup-all.sh

# Make executable
chmod +x setup-all.sh

cd ..
```

### Step 8: Master Documentation Creation

**Purpose**: Create comprehensive README for the apps directory

**Commands**:
```bash
# Create master README
touch apps/README.md
```

---

## Complete File Contents

This section contains the complete content of every file created during the setup process. Copy these contents exactly to reproduce the implementation.

### Root .gitignore

**File**: `.gitignore`

```gitignore
# Virtual Environments
**/.venv/
**/venv/
**/env/

# Node modules
**/node_modules/

# Output files
**/output/*.pptx
**/output/*.pdf
**/output/*.html
**/output/*.png
**/output/*.jpg

# Python
**/__pycache__/
**/*.pyc
**/.pytest_cache/
**/*.egg-info/

# IDE files
.idea/
.vscode/
*.swp
*.swo

# OS files
.DS_Store
Thumbs.db

# Temporary files
**/tmp/
**/temp/

# Log files
**/*.log

# Config files with secrets
**/.env
**/config/secrets.json
```

### Automation Script

**File**: `apps/setup-all.sh` (The complete automated setup script)

```bash
#!/bin/bash

# Setup script for all markdown-to-slides conversion approaches
# Creates virtual environments and installs dependencies

echo "🚀 Setting up all Markdown-to-Slides conversion approaches"
echo "=========================================================="

# Change to apps directory
cd "$(dirname "$0")"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print status
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

# Check prerequisites
print_status "Checking prerequisites..."

# Check Python
if ! command -v python3 &> /dev/null; then
    print_error "Python3 not found. Please install Python 3.8+"
    exit 1
fi
print_success "Python3 found: $(python3 --version)"

# Check Node.js
if ! command -v node &> /dev/null; then
    print_warning "Node.js not found. Node.js projects will be skipped."
    NODE_AVAILABLE=false
else
    print_success "Node.js found: $(node --version)"
    NODE_AVAILABLE=true
fi

# Check npm
if ! command -v npm &> /dev/null; then
    print_warning "npm not found. Node.js projects will be skipped."
    NPM_AVAILABLE=false
else
    print_success "npm found: $(npm --version)"
    NPM_AVAILABLE=true
fi

echo ""

# Setup Python projects
PYTHON_PROJECTS=("03-md2pptx-python" "04-pandoc-universal" "05-python-pptx-custom" "06-presenton-ai")

for project in "${PYTHON_PROJECTS[@]}"; do
    if [ -d "$project" ]; then
        print_status "Setting up $project..."

        cd "$project"

        # Create virtual environment
        if [ ! -d ".venv" ]; then
            print_status "Creating virtual environment..."
            python3 -m venv .venv
        fi

        # Activate and install requirements
        if [ -f "requirements.txt" ]; then
            print_status "Installing Python dependencies..."
            source .venv/bin/activate
            pip install --upgrade pip
            pip install -r requirements.txt
            deactivate
            print_success "$project setup completed"
        else
            print_warning "No requirements.txt found for $project"
        fi

        cd ..
        echo ""
    else
        print_warning "Directory $project not found, skipping..."
    fi
done

# Setup Node.js projects
if [ "$NODE_AVAILABLE" = true ] && [ "$NPM_AVAILABLE" = true ]; then
    NODE_PROJECTS=("01-marp-cli" "02-slidev")

    for project in "${NODE_PROJECTS[@]}"; do
        if [ -d "$project" ]; then
            print_status "Setting up $project..."

            cd "$project"

            if [ -f "package.json" ]; then
                print_status "Installing Node.js dependencies..."
                npm install
                print_success "$project setup completed"
            else
                print_warning "No package.json found for $project"
            fi

            cd ..
            echo ""
        else
            print_warning "Directory $project not found, skipping..."
        fi
    done
else
    print_warning "Skipping Node.js projects (Node.js/npm not available)"
fi

# Final status
echo ""
print_success "Setup completed for all available projects!"
echo ""
print_status "Available conversion approaches:"
echo "  📝 01-marp-cli (Node.js) - Simple PPTX export"
echo "  🌍 04-pandoc-universal (Python) - Universal converter"
echo "  🐍 03-md2pptx-python (Python) - Custom Python solution"
echo ""
print_status "Test with shared input file:"
echo "  📄 apps/shared/input/gcp-cert-prep-slides-v2.md"
echo ""
print_status "To test conversions:"
echo "  cd 01-marp-cli && ./scripts/convert.sh"
echo "  cd 04-pandoc-universal && ./scripts/convert.sh"
echo "  cd 03-md2pptx-python && source .venv/bin/activate && python scripts/convert.py ../shared/input/gcp-cert-prep-slides-v2.md output/test.pptx"
```

---

## Verification Steps

After completing the implementation, verify your setup with these steps:

### 1. Directory Structure Verification

```bash
# Check overall structure
tree apps/ -L 2

# Expected output:
apps/
├── 01-marp-cli/
│   ├── node_modules/
│   ├── output/
│   ├── package.json
│   ├── README.md
│   └── scripts/
├── 03-md2pptx-python/
│   ├── .venv/
│   ├── output/
│   ├── README.md
│   ├── requirements.txt
│   └── scripts/
├── 04-pandoc-universal/
│   ├── .venv/
│   ├── output/
│   ├── README.md
│   ├── requirements.txt
│   └── scripts/
├── shared/
│   ├── input/
│   ├── README.md
│   └── templates/
├── README.md
└── setup-all.sh
```

### 2. Test Shared Input File

```bash
# Verify GCP test content exists
ls -la apps/shared/input/
cat apps/shared/input/gcp-cert-prep-slides-v2.md | head -20

# Should show:
# GCP Cloud Architect Certification Prep
# ## Towards a More Sustainable Approach
# ---
# ## Slide 1: Who Doesn't Love Studying...
```

### 3. Virtual Environment Verification

```bash
# Check Python virtual environments exist
ls -la apps/03-md2pptx-python/.venv/
ls -la apps/04-pandoc-universal/.venv/

# Test Python virtual environment activation
cd apps/03-md2pptx-python
source .venv/bin/activate
python --version  # Should show Python 3.8+
pip list          # Should show installed packages
deactivate
cd ../..
```

### 4. Node.js Setup Verification

```bash
# Check Marp CLI installation
cd apps/01-marp-cli
npm list @marp-team/marp-cli  # Should show version
npx marp --version            # Should show Marp CLI version
cd ../..
```

### 5. Automated Setup Script Test

```bash
# Run the automated setup script
cd apps
chmod +x setup-all.sh
./setup-all.sh

# Expected output:
# 🚀 Setting up all Markdown-to-Slides conversion approaches
# [INFO] Checking prerequisites...
# [SUCCESS] Python3 found: Python 3.x.x
# [SUCCESS] Node.js found: vx.x.x
# [SUCCESS] npm found: x.x.x
# [SUCCESS] Setup completed for all available projects!
```

---

## Usage Examples

### Quick Start - Test All Approaches

```bash
# 1. Run automated setup
cd apps
./setup-all.sh

# 2. Test Marp CLI conversion
cd 01-marp-cli
./scripts/convert.sh
ls -la output/*.pptx

# 3. Test Pandoc Universal conversion
cd ../04-pandoc-universal
./scripts/convert.sh
ls -la output/*.pptx

# 4. Test Python md2pptx conversion
cd ../03-md2pptx-python
source .venv/bin/activate
python scripts/convert.py ../shared/input/gcp-cert-prep-slides-v2.md output/gcp-slides.pptx
ls -la output/*.pptx
deactivate

cd ../..
```

### Individual Approach Usage

**Marp CLI (Simplest)**:
```bash
cd apps/01-marp-cli

# Basic conversion
npx marp ../shared/input/gcp-cert-prep-slides-v2.md --pptx -o output/slides.pptx

# With custom theme (if available)
npx marp ../shared/input/gcp-cert-prep-slides-v2.md --pptx --theme config/custom.css -o output/themed-slides.pptx

# Watch mode for development
npx marp --watch ../shared/input/gcp-cert-prep-slides-v2.md --pptx -o output/live-slides.pptx
```

**Pandoc Universal (Best Quality)**:
```bash
cd apps/04-pandoc-universal

# Direct pandoc conversion
pandoc ../shared/input/gcp-cert-prep-slides-v2.md -t pptx -o output/pandoc-slides.pptx

# Using Python wrapper script
source .venv/bin/activate
python scripts/convert.py ../shared/input/gcp-cert-prep-slides-v2.md output/python-wrapper-slides.pptx
deactivate

# Using bash script (multiple variants)
./scripts/convert.sh
```

**Python md2pptx (Most Customizable)**:
```bash
cd apps/03-md2pptx-python
source .venv/bin/activate

# Basic conversion
python scripts/convert.py ../shared/input/gcp-cert-prep-slides-v2.md output/python-slides.pptx

# With table of contents (if implemented)
python scripts/convert.py ../shared/input/gcp-cert-prep-slides-v2.md output/slides-with-toc.pptx --toc

# With custom template (if available)
python scripts/convert.py ../shared/input/gcp-cert-prep-slides-v2.md output/templated-slides.pptx --template config/template.pptx

deactivate
```

### Batch Processing Example

```bash
# Process multiple markdown files with Marp CLI
cd apps/01-marp-cli
mkdir -p input
cp ../shared/input/*.md input/
npx marp input/*.md --pptx --output-dir output/

# Process with Pandoc
cd ../04-pandoc-universal
for file in ../shared/input/*.md; do
    basename=$(basename "$file" .md)
    pandoc "$file" -t pptx -o "output/${basename}.pptx"
done
```

---

## Troubleshooting

### Common Issues and Solutions

#### 1. Virtual Environment Problems

**Problem**: `python3 -m venv .venv` fails
```bash
# Solution: Install python3-venv package
sudo apt install python3-venv

# Or use alternative method
python3 -m pip install --user virtualenv
python3 -m virtualenv .venv
```

**Problem**: Virtual environment activation fails
```bash
# Check if .venv directory exists
ls -la .venv/

# Recreate if corrupted
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
```

#### 2. Node.js/npm Issues

**Problem**: `npm install` fails with permission errors
```bash
# Solution: Use Node Version Manager (recommended)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc
nvm install --lts
nvm use --lts

# Or configure npm global directory
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

**Problem**: Marp CLI not found after installation
```bash
# Use npx to run without global installation
npx @marp-team/marp-cli --version

# Or install globally
npm install -g @marp-team/marp-cli
marp --version
```

#### 3. Pandoc Installation Issues

**Problem**: Pandoc not found
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install pandoc

# macOS
brew install pandoc

# Or download directly from pandoc.org
wget https://github.com/jgm/pandoc/releases/download/3.1.8/pandoc-3.1.8-1-amd64.deb
sudo dpkg -i pandoc-3.1.8-1-amd64.deb
```

**Problem**: Pandoc version too old
```bash
# Check version (need 2.0+)
pandoc --version

# Remove old version and install latest
sudo apt remove pandoc
# Follow installation instructions above
```

#### 4. Python Dependencies Issues

**Problem**: `pip install -r requirements.txt` fails
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Install with verbose output to see errors
pip install -v -r requirements.txt

# Install packages individually if needed
pip install python-pptx
pip install markdown
pip install requests
pip install Pillow
```

**Problem**: python-pptx import errors
```bash
# Check if properly installed in virtual environment
source .venv/bin/activate
python -c "import pptx; print(pptx.__version__)"

# Reinstall if needed
pip uninstall python-pptx
pip install python-pptx>=0.6.21
```

#### 5. File Permission Issues

**Problem**: Scripts not executable
```bash
# Make all scripts executable
find apps/ -name "*.sh" -exec chmod +x {} \;
find apps/ -name "*.py" -exec chmod +x {} \;

# Or individually
chmod +x apps/setup-all.sh
chmod +x apps/01-marp-cli/scripts/convert.sh
chmod +x apps/03-md2pptx-python/scripts/convert.py
chmod +x apps/04-pandoc-universal/scripts/convert.py
chmod +x apps/04-pandoc-universal/scripts/convert.sh
```

#### 6. Output Directory Issues

**Problem**: "No such file or directory" errors
```bash
# Ensure output directories exist
mkdir -p apps/01-marp-cli/output
mkdir -p apps/03-md2pptx-python/output
mkdir -p apps/04-pandoc-universal/output

# Or let scripts create them automatically (most scripts do this)
```

#### 7. Git Issues

**Problem**: Virtual environments committed to git
```bash
# Check .gitignore is working
git status

# Should NOT show .venv/ directories or node_modules/

# If showing, ensure .gitignore is correct and run:
git rm -r --cached apps/*/.venv/
git rm -r --cached apps/*/node_modules/
git commit -m "Remove virtual environments from git"
```

#### 8. Input File Issues

**Problem**: "Input file not found" errors
```bash
# Verify test file exists
ls -la apps/shared/input/gcp-cert-prep-slides-v2.md

# Copy if missing
cp rnd/gcp-cert-prep-slides-v2.md apps/shared/input/

# Check file permissions
chmod 644 apps/shared/input/gcp-cert-prep-slides-v2.md
```

### Getting Help

If you encounter issues not covered here:

1. Check individual project README files for specific troubleshooting
2. Verify all prerequisites are installed with correct versions
3. Run the automated setup script with verbose output
4. Check system logs for detailed error messages
5. Consider using Docker for isolated environments (advanced)

### System Requirements Verification

```bash
# Check all requirements at once
echo "=== System Requirements Check ==="
echo "Python: $(python3 --version 2>/dev/null || echo 'NOT FOUND')"
echo "Node.js: $(node --version 2>/dev/null || echo 'NOT FOUND')"
echo "npm: $(npm --version 2>/dev/null || echo 'NOT FOUND')"
echo "Pandoc: $(pandoc --version 2>/dev/null | head -1 || echo 'NOT FOUND')"
echo "Git: $(git --version 2>/dev/null || echo 'NOT FOUND')"
echo "============================="
```

---

**End of Setup Guide**

This comprehensive guide provides everything needed to reproduce the markdown-to-slides conversion setup from scratch. Each approach offers different advantages, and the automated setup script makes it easy to test all methods and choose the best one for your specific needs.

---