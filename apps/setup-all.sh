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