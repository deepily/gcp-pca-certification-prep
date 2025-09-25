#!/usr/bin/env python3
"""
Pandoc-based Markdown to PPTX Converter
Wrapper script for enhanced Pandoc functionality
"""

import argparse
import subprocess
import sys
from pathlib import Path


def run_pandoc( input_file, output_file, template=None, slide_level=2 ):
    """Run pandoc conversion with specified parameters"""

    cmd = [
        'pandoc',
        input_file,
        '-t', 'pptx',
        '-o', output_file,
        f'--slide-level={slide_level}'
    ]

    if template and Path( template ).exists():
        cmd.extend( ['--reference-doc', template] )

    print( f"🔧 Running: {' '.join( cmd )}" )

    try:
        result = subprocess.run( cmd, capture_output=True, text=True, check=True )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr
    except FileNotFoundError:
        return False, "Pandoc not found. Please install pandoc: sudo apt-get install pandoc"


def main():
    parser = argparse.ArgumentParser( description='Convert Markdown to PPTX using Pandoc' )
    parser.add_argument( 'input_file', help='Input markdown file' )
    parser.add_argument( 'output_file', help='Output PPTX file' )
    parser.add_argument( '--template', help='PowerPoint reference template' )
    parser.add_argument( '--slide-level', type=int, default=2, help='Slide level (default: 2)' )

    args = parser.parse_args()

    # Verify input file exists
    input_path = Path( args.input_file )
    if not input_path.exists():
        print( f"❌ Input file not found: {args.input_file}" )
        return 1

    # Create output directory
    output_path = Path( args.output_file )
    output_path.parent.mkdir( parents=True, exist_ok=True )

    print( f"📝 Converting {args.input_file} to {args.output_file}..." )
    print( f"🎯 Slide level: {args.slide_level}" )

    if args.template:
        print( f"🎨 Using template: {args.template}" )

    # Run conversion
    success, message = run_pandoc(
        args.input_file,
        args.output_file,
        args.template,
        args.slide_level
    )

    if success:
        print( f"✅ Conversion completed successfully!" )
        print( f"📁 Output: {args.output_file}" )

        # Show file info
        if output_path.exists():
            size_mb = output_path.stat().st_size / (1024 * 1024)
            print( f"📊 File size: {size_mb:.2f} MB" )

        return 0
    else:
        print( f"❌ Conversion failed: {message}" )
        return 1


if __name__ == '__main__':
    exit( main() )