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

| Approach | Status | Output Type | Editable Text | File Size | Speed |
|----------|--------|-------------|---------------|-----------|-------|
| **Pandoc Universal** | ✅ Working | Native PPTX | ✅ | 44-70KB | 2-4s |
| **Python md2pptx** | ✅ Working | Native PPTX | ✅ | 42KB | 1-2s |
| **Marp CLI** | ❌ PPTX Broken | Images in PPTX | ❌ | Timeout | Failed |

## 📁 **Generated Output Files - Ready to Use**

### 🏆 **Production-Ready PPTX Files**

| File | Location | Size | Description |
|------|----------|------|-------------|
| **🥇 gcp-slides-with-notes.pptx** | `04-pandoc-universal/output/` | 70KB | **BEST OVERALL** - With rich presenter notes |
| **🥈 gcp-slides-python.pptx** | `03-md2pptx-python/output/` | 42KB | **FASTEST** - Python-generated, clean formatting |
| **gcp-slides-basic.pptx** | `04-pandoc-universal/output/` | 44KB | Basic Pandoc conversion |
| **gcp-slides-advanced.pptx** | `04-pandoc-universal/output/` | 44KB | Enhanced Pandoc with slide-level=2 |
| **gcp-slides-metadata.pptx** | `04-pandoc-universal/output/` | 45KB | With presentation metadata |

### 📋 **Quick Access Commands**

```bash
# Copy best overall file to desktop
cp 04-pandoc-universal/output/gcp-slides-with-notes.pptx ~/Desktop/

# Copy fastest-generated file
cp 03-md2pptx-python/output/gcp-slides-python.pptx ~/Desktop/

# View all generated files
ls -lh */output/*.pptx

# Open best file directly
open 04-pandoc-universal/output/gcp-slides-with-notes.pptx
```

## 💡 Recommendations

**🥇 For Google Slides import with presenter notes**: Use Pandoc Universal with Notes
- File: `04-pandoc-universal/output/gcp-slides-with-notes.pptx`
- Rich presenter notes from blog post integration
- Perfect Google Slides compatibility

**🥈 For speed and simplicity**: Use Python md2pptx
- File: `03-md2pptx-python/output/gcp-slides-python.pptx`
- Fastest conversion (1-2 seconds)
- Smallest file size (42KB)
- Clean, professional formatting

**⚠️ Avoid**: Marp CLI for PPTX export
- PPTX export functionality is fundamentally broken (timeout issues)
- HTML export still works for web presentations
- Not recommended for PowerPoint/Google Slides workflows

### 🚀 **Master Conversion Script**

Use the unified conversion interface:
```bash
# Generate with presenter notes (recommended)
python master-convert.py shared/input/gcp-cert-prep-slides-v2.md --approach pandoc-with-notes

# Generate fastest version
python master-convert.py shared/input/gcp-cert-prep-slides-v2.md --approach python-md2pptx

# Compare all approaches
python master-convert.py shared/input/gcp-cert-prep-slides-v2.md --approach all-approaches
```

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