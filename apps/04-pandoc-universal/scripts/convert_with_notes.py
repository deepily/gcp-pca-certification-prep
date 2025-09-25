#!/usr/bin/env python3
"""
Enhanced Pandoc Conversion with Presenter Notes
Combines slides with blog post content for rich presenter notes
"""

import sys
import subprocess
import tempfile
from pathlib import Path
import re

# Add the shared scripts to the path
sys.path.append( str( Path( __file__ ).parent.parent.parent / "shared" / "scripts" ) )

from blog_to_notes_mapper import BlogToNotesMapper


def create_enhanced_slides_with_notes( slides_path: str, blog_path: str, output_path: str ):
    """Create enhanced slides markdown with presenter notes"""

    # Generate presenter notes mapping
    mapper = BlogToNotesMapper( blog_path, slides_path )
    notes_mapping = mapper.generate_notes_mapping()

    # Read original slides
    with open( slides_path, 'r', encoding='utf-8' ) as f:
        slides_content = f.read()

    # Parse slides and add notes
    enhanced_content = []
    slide_blocks = slides_content.split( '---' )

    for i, block in enumerate( slide_blocks ):
        block = block.strip()
        if not block:
            continue

        # Add the slide content
        enhanced_content.append( block )

        # Extract slide title for notes matching
        title_match = re.search( r'##\s+Slide\s+\d+:\s*(.+)', block )
        if not title_match:
            title_match = re.search( r'##\s+(.+)', block )

        if title_match:
            slide_title = title_match.group( 1 ).strip()

            # Find matching notes
            notes = None
            for notes_title, notes_content in notes_mapping.items():
                if slide_title.lower() in notes_title.lower() or notes_title.lower() in slide_title.lower():
                    notes = notes_content
                    break

            if notes:
                # Add speaker notes section
                enhanced_content.append( "\n::: notes" )
                enhanced_content.append( notes.strip() )
                enhanced_content.append( ":::" )

        # Add slide separator
        enhanced_content.append( "---" )

    # Remove the last separator
    if enhanced_content and enhanced_content[-1] == "---":
        enhanced_content.pop()

    # Write enhanced slides
    with open( output_path, 'w', encoding='utf-8' ) as f:
        f.write( '\n\n'.join( enhanced_content ) )

    print( f"✅ Enhanced slides with notes created: {output_path}" )


def run_pandoc_conversion( enhanced_slides_path: str, output_dir: str ):
    """Run Pandoc conversions with the enhanced slides"""

    output_path = Path( output_dir )
    output_path.mkdir( parents=True, exist_ok=True )

    # Basic conversion with notes
    print( "📝 Converting with presenter notes..." )
    cmd = [
        "pandoc",
        enhanced_slides_path,
        "-t", "pptx",
        "--slide-level=2",
        "--metadata", "title=GCP Certification Prep - Enhanced with Notes",
        "-o", str( output_path / "gcp-slides-with-notes.pptx" )
    ]

    try:
        result = subprocess.run( cmd, check=True, capture_output=True, text=True )
        print( "✅ Enhanced PPTX with presenter notes generated!" )
        return True
    except subprocess.CalledProcessError as e:
        print( f"❌ Pandoc conversion failed: {e.stderr}" )
        return False


def main():
    """Main function"""
    import argparse

    parser = argparse.ArgumentParser( description='Enhanced Pandoc conversion with presenter notes' )
    parser.add_argument( '--slides', default='../shared/input/gcp-cert-prep-slides-v2.md', help='Slides markdown file' )
    parser.add_argument( '--blog', default='../../rnd/gcp-cloud-certification-blog-post.md', help='Blog post markdown file' )
    parser.add_argument( '--output-dir', default='output', help='Output directory for PPTX files' )

    args = parser.parse_args()

    print( "🎯 Enhanced Pandoc Conversion with Presenter Notes" )
    print( "=================================================" )

    # Check if pandoc is available
    try:
        subprocess.run( ["pandoc", "--version"], check=True, capture_output=True )
    except (subprocess.CalledProcessError, FileNotFoundError):
        print( "❌ Pandoc not found. Please install:" )
        print( "   sudo apt-get update && sudo apt-get install pandoc" )
        return 1

    # Create temporary enhanced slides file
    with tempfile.NamedTemporaryFile( mode='w', suffix='.md', delete=False, encoding='utf-8' ) as tmp:
        temp_slides_path = tmp.name

    try:
        # Create enhanced slides with notes
        create_enhanced_slides_with_notes( args.slides, args.blog, temp_slides_path )

        # Run Pandoc conversion
        if run_pandoc_conversion( temp_slides_path, args.output_dir ):
            # Show results
            output_path = Path( args.output_dir )
            print( "\n📁 Generated files:" )
            for pptx_file in output_path.glob( "*.pptx" ):
                file_size = pptx_file.stat().st_size / 1024  # KB
                print( f"  {pptx_file.name} ({file_size:.1f} KB)" )

            print( "\n🎉 Enhanced conversion completed!" )
            print( "💡 PPTX files now include rich presenter notes" )
            print( "📤 Import into Google Slides to see speaker notes" )
            return 0
        else:
            return 1

    finally:
        # Clean up temporary file
        Path( temp_slides_path ).unlink( missing_ok=True )


if __name__ == '__main__':
    exit( main() )