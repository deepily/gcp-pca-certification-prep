# Markdown to Slides Conversion Approaches

This directory contains multiple implementations for converting markdown presentations to various output formats, primarily targeting Google Slides compatibility through PPTX generation.

## 🎯 Quick Start

```bash
# Setup all projects at once
./setup-all.sh

# Or setup individually per project README
```

## 📁 Directory Structure

```
apps/
├── 01-marp-cli/           # Marp CLI - Simplest approach (Node.js)
├── 02-slidev/             # Slidev - Modern Vue.js-based (Node.js)
├── 03-md2pptx-python/     # Custom Python PPTX generator
├── 04-pandoc-universal/   # Pandoc - Universal converter
├── 05-python-pptx-custom/ # Direct python-pptx implementation
├── 06-presenton-ai/       # AI-powered with image generation
├── shared/                # Common test files and templates
└── setup-all.sh           # Automated setup script
```

## 🚀 Conversion Approaches

### 1. Marp CLI (Recommended for simplicity)
- **Type**: Node.js CLI tool
- **Output**: PPTX (image-based)
- **Pros**: Mature, stable, direct PPTX export
- **Setup**: `cd 01-marp-cli && npm install`
- **Usage**: `npx marp input.md --pptx -o output.pptx`

### 2. Pandoc Universal (Recommended for quality)
- **Type**: Universal document converter
- **Output**: PPTX (editable text)
- **Pros**: Highest quality, editable output
- **Setup**: Install pandoc + `cd 04-pandoc-universal && source .venv/bin/activate`
- **Usage**: `pandoc input.md -t pptx -o output.pptx`

### 3. md2pptx Python
- **Type**: Custom Python solution
- **Output**: PPTX (editable text)
- **Pros**: Template support, production-tested
- **Setup**: `cd 03-md2pptx-python && source .venv/bin/activate`
- **Usage**: `python scripts/convert.py input.md output.pptx`

## 📊 Test Content

All approaches use the same test file for comparison:
- **Input**: `shared/input/gcp-cert-prep-slides-v2.md`
- **Content**: 15-slide GCP certification presentation
- **Format**: Standard markdown with `---` slide delimiters

## 🎨 Output Comparison

| Approach | Output Type | Editable Text | File Size | Setup Complexity |
|----------|-------------|---------------|-----------|------------------|
| Marp CLI | Images in PPTX | ❌ | Small | Low |
| Pandoc | Native PPTX | ✅ | Medium | Medium |
| md2pptx | Native PPTX | ✅ | Medium | Medium |

## 💡 Recommendations

**For beginners**: Start with Marp CLI
- Easiest setup and usage
- Direct PPTX output works well for basic needs

**For best results**: Use Pandoc Universal
- Generates editable text (not images)
- Imports perfectly into Google Slides
- Most flexible and feature-rich

**For customization**: Use md2pptx Python
- Template support
- Advanced markdown features
- Production-grade solution

## 🔧 Prerequisites

### Required
- Python 3.8+ (for Python-based solutions)
- Node.js 16+ (for Marp CLI and Slidev)

### Optional
- Pandoc system installation (for Pandoc Universal)
- Docker (for advanced AI integration)

## 📚 Next Steps

1. Run `./setup-all.sh` to configure all approaches
2. Test each approach with the shared GCP content
3. Compare output quality and choose your preferred method
4. Customize templates and themes as needed

## 🛠️ Troubleshooting

- **Virtual environment issues**: Ensure Python 3.8+ is installed
- **Node.js problems**: Update to Node.js 16 or later
- **Pandoc not found**: Install via `sudo apt-get install pandoc`
- **Permission errors**: Run `chmod +x scripts/*.sh` in each project

Each project directory contains detailed setup and usage instructions in its README.md file.