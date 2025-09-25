# Marp CLI - Markdown to PPTX Conversion

The simplest and most mature solution for converting markdown to PPTX presentations.

## About

- **GitHub**: @marp-team/marp-cli (9.6k stars)
- **Type**: Node.js CLI tool
- **Output**: PPTX (PowerPoint compatible)
- **Approach**: Pre-rendered high-resolution images in PPTX format

## Setup

```bash
# Install dependencies (already done)
npm install

# Or install globally
npm install -g @marp-team/marp-cli
```

## Usage

### Basic Conversion
```bash
# Convert single file
npx marp ../shared/input/gcp-cert-prep-slides-v2.md --pptx -o output/gcp-slides.pptx

# Convert with custom theme
npx marp ../shared/input/gcp-cert-prep-slides-v2.md --pptx --theme config/custom.css -o output/gcp-slides-themed.pptx

# Watch mode for development
npx marp --watch ../shared/input/gcp-cert-prep-slides-v2.md --pptx -o output/gcp-slides.pptx
```

### Batch Processing
```bash
# Convert all markdown files
npx marp input/*.md --pptx
```

## Configuration

- Custom CSS themes in `config/` directory
- PPTX output options: `--pptx-editable` for experimental text editing
- Scale factor: default 2x for high-resolution output

## Pros
- ✅ Mature and stable
- ✅ Direct PPTX export
- ✅ Custom CSS theming
- ✅ Batch processing
- ✅ Docker support available

## Cons
- ❌ Output is image-based (not editable text)
- ❌ Limited interactive features
- ❌ No built-in AI integration

## Test Results

Test with shared GCP certification content to compare output quality with other approaches.