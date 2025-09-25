# Pandoc Universal - Maximum Flexibility Converter

Universal document converter with native editable PPTX output and extensive format support.

## About

- **GitHub**: jgm/pandoc (39.2k stars)
- **Type**: Universal document converter
- **Output**: Editable PPTX with actual text and shapes
- **Approach**: Direct PowerPoint generation (not images)

## Setup

### System Requirements
```bash
# Install Pandoc system-wide (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install pandoc

# Or download from: https://pandoc.org/installing.html
```

### Python Environment
```bash
# Activate virtual environment
source .venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

## Features

- ✅ Editable PPTX output (actual text, not images)
- ✅ Custom PowerPoint templates via `--reference-doc`
- ✅ 50+ input/output format support
- ✅ LaTeX math rendering
- ✅ Automatic bibliographies
- ✅ Complex markdown features

## Usage

### Basic Conversion
```bash
# Direct pandoc conversion
pandoc ../shared/input/gcp-cert-prep-slides-v2.md -t pptx -o output/gcp-slides-basic.pptx

# With custom template
pandoc ../shared/input/gcp-cert-prep-slides-v2.md -t pptx --reference-doc=config/template.pptx -o output/gcp-slides-templated.pptx
```

### Advanced Features
```bash
# With metadata and custom settings
pandoc ../shared/input/gcp-cert-prep-slides-v2.md -t pptx --slide-level=2 -o output/gcp-slides-advanced.pptx

# Using the conversion script
source .venv/bin/activate
python scripts/convert.py ../shared/input/gcp-cert-prep-slides-v2.md output/gcp-slides.pptx
```

## Configuration

- Reference templates in `config/` directory
- Slide level configuration (`--slide-level`)
- Math and citation support
- Custom CSS for styling

## Pros
- ✅ Most flexible converter available
- ✅ Editable text output (not images)
- ✅ Extensive format support
- ✅ Custom template support
- ✅ Academic features (math, citations)
- ✅ Mature and well-documented

## Cons
- ❌ System dependency (Pandoc installation)
- ❌ Learning curve for advanced features
- ❌ More complex than simple solutions

## Test Results

Pandoc generates the highest quality editable PPTX files that import perfectly into Google Slides.