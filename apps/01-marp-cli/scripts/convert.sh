#!/bin/bash

# Marp CLI Conversion Script
# Converts markdown files to PPTX using Marp CLI

echo "🎯 Marp CLI - Markdown to PPTX Converter"
echo "========================================"

# Create output directory if it doesn't exist
mkdir -p output

# Basic conversion
echo "📝 Converting GCP certification slides..."
npx marp ../shared/input/gcp-cert-prep-slides-v2.md --pptx -o output/gcp-slides-basic.pptx

if [ $? -eq 0 ]; then
    echo "✅ Basic conversion completed: output/gcp-slides-basic.pptx"
else
    echo "❌ Basic conversion failed"
    exit 1
fi

# Conversion with high quality settings
echo "📝 Converting with high quality settings..."
npx marp ../shared/input/gcp-cert-prep-slides-v2.md --pptx --pdf-notes -o output/gcp-slides-hq.pptx

if [ $? -eq 0 ]; then
    echo "✅ High quality conversion completed: output/gcp-slides-hq.pptx"
else
    echo "❌ High quality conversion failed"
fi

# Show output files
echo ""
echo "📁 Generated files:"
ls -lh output/*.pptx 2>/dev/null || echo "No PPTX files found in output directory"

echo ""
echo "🎉 Marp CLI conversion completed!"
echo "Import the PPTX files into Google Slides for final editing."