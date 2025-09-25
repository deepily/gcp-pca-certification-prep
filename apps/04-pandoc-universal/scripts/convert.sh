#!/bin/bash

# Pandoc Universal Conversion Script
# Multiple conversion approaches using Pandoc

echo "🌍 Pandoc Universal - Markdown to PPTX Converter"
echo "================================================"

# Check if pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo "❌ Pandoc not found. Please install:"
    echo "   sudo apt-get update && sudo apt-get install pandoc"
    exit 1
fi

# Create output directory
mkdir -p output

# Basic conversion
echo "📝 Basic Pandoc conversion..."
pandoc ../shared/input/gcp-cert-prep-slides-v2.md -t pptx -o output/gcp-slides-basic.pptx

if [ $? -eq 0 ]; then
    echo "✅ Basic conversion completed: output/gcp-slides-basic.pptx"
else
    echo "❌ Basic conversion failed"
fi

# Advanced conversion with custom slide level
echo "📝 Advanced conversion (slide-level=2)..."
pandoc ../shared/input/gcp-cert-prep-slides-v2.md -t pptx --slide-level=2 -o output/gcp-slides-advanced.pptx

if [ $? -eq 0 ]; then
    echo "✅ Advanced conversion completed: output/gcp-slides-advanced.pptx"
else
    echo "❌ Advanced conversion failed"
fi

# Conversion with metadata
echo "📝 Conversion with metadata..."
pandoc ../shared/input/gcp-cert-prep-slides-v2.md -t pptx --slide-level=2 --metadata title="GCP Certification Prep" -o output/gcp-slides-metadata.pptx

if [ $? -eq 0 ]; then
    echo "✅ Metadata conversion completed: output/gcp-slides-metadata.pptx"
else
    echo "❌ Metadata conversion failed"
fi

# Show results
echo ""
echo "📁 Generated files:"
ls -lh output/*.pptx 2>/dev/null || echo "No PPTX files found in output directory"

echo ""
echo "🎉 Pandoc conversion completed!"
echo "💡 These PPTX files contain editable text (not images)"
echo "📤 Import directly into Google Slides for best results"