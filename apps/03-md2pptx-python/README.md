# md2pptx Python - Production Markdown to PPTX Converter

Python-based solution for converting markdown to PPTX with template support and advanced features.

## About

- **GitHub**: MartinPacker/md2pptx
- **Type**: Python CLI tool using python-pptx
- **Output**: PPTX (editable PowerPoint)
- **Approach**: Direct PPTX generation with custom layouts

## Setup

```bash
# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Features

- ✅ PowerPoint templates support
- ✅ Table of contents generation
- ✅ Task lists and checkboxes
- ✅ Glossary slides
- ✅ Critic Markup for reviews
- ✅ Editable text output (not images)

## Usage

### Basic Conversion
```bash
# Activate environment first
source .venv/bin/activate

# Convert markdown to PPTX
python scripts/convert.py ../shared/input/gcp-cert-prep-slides-v2.md output/gcp-slides.pptx

# Or using Unix pipeline style
python scripts/md2pptx.py output/gcp-slides.pptx < ../shared/input/gcp-cert-prep-slides-v2.md
```

### Advanced Features
```bash
# With custom template
python scripts/convert.py ../shared/input/gcp-cert-prep-slides-v2.md output/gcp-slides-templated.pptx --template config/gcp-template.pptx

# Generate table of contents
python scripts/convert.py ../shared/input/gcp-cert-prep-slides-v2.md output/gcp-slides-toc.pptx --toc
```

## Configuration

- Custom PowerPoint templates in `config/` directory
- Slide layouts and styling options
- Image handling and embedding

## Pros
- ✅ Editable text output (not images)
- ✅ Production-tested solution
- ✅ PowerPoint template support
- ✅ Complex markdown features
- ✅ Table of contents generation

## Cons
- ❌ Python dependency management
- ❌ More complex setup than Marp
- ❌ No built-in themes like Marp

## Test Results

Test with shared GCP certification content to compare output quality and editability.