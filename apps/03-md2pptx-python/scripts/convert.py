#!/usr/bin/env python3
"""
Simple Markdown to PPTX Converter
Based on python-pptx library for direct PPTX generation
"""

import argparse
import re
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
import markdown


def parse_markdown_slides( md_content ):
    """Parse markdown content into individual slides"""
    # Split on slide delimiters
    slides = re.split( r'^---\s*$', md_content, flags=re.MULTILINE )

    parsed_slides = []
    for slide_content in slides:
        slide_content = slide_content.strip()
        if not slide_content:
            continue

        # Extract title (first heading)
        title_match = re.search( r'^##?\s+(.+)', slide_content, re.MULTILINE )
        title = title_match.group( 1 ) if title_match else "Untitled Slide"

        # Extract bullet points
        bullets = re.findall( r'^\s*[-*]\s+(.+)', slide_content, re.MULTILINE )

        # Extract content after title
        content_lines = []
        lines = slide_content.split( '\n' )
        found_title = False

        for line in lines:
            if re.match( r'^##?\s+', line ):
                found_title = True
                continue
            if found_title and line.strip():
                if not line.strip().startswith( '-' ) and not line.strip().startswith( '*' ):
                    content_lines.append( line.strip() )

        parsed_slides.append({
            'title': title,
            'bullets': bullets,
            'content': '\n'.join( content_lines )
        })

    return parsed_slides


def create_presentation( slides ):
    """Create PPTX presentation from parsed slides"""
    prs = Presentation()

    for slide_data in slides:
        # Use title and content layout
        slide_layout = prs.slide_layouts[1]  # Title and Content layout
        slide = prs.slides.add_slide( slide_layout )

        # Set title
        title = slide.shapes.title
        title.text = slide_data['title']

        # Add content
        if slide_data['bullets']:
            # Add bullet points
            content = slide.placeholders[1]
            tf = content.text_frame
            tf.text = slide_data['bullets'][0]

            for bullet in slide_data['bullets'][1:]:
                p = tf.add_paragraph()
                p.text = bullet
                p.level = 0
        elif slide_data['content']:
            # Add regular content
            content = slide.placeholders[1]
            content.text = slide_data['content']

    return prs


def main():
    parser = argparse.ArgumentParser( description='Convert Markdown to PPTX' )
    parser.add_argument( 'input_file', help='Input markdown file' )
    parser.add_argument( 'output_file', help='Output PPTX file' )
    parser.add_argument( '--template', help='PowerPoint template file' )
    parser.add_argument( '--toc', action='store_true', help='Generate table of contents' )

    args = parser.parse_args()

    # Read input file
    input_path = Path( args.input_file )
    if not input_path.exists():
        print( f"❌ Input file not found: {args.input_file}" )
        return 1

    print( f"📝 Reading {args.input_file}..." )
    with open( input_path, 'r', encoding='utf-8' ) as f:
        md_content = f.read()

    # Parse slides
    print( "🔍 Parsing markdown slides..." )
    slides = parse_markdown_slides( md_content )
    print( f"📊 Found {len( slides )} slides" )

    # Create presentation
    print( "🎯 Creating PPTX presentation..." )
    prs = create_presentation( slides )

    # Save presentation
    output_path = Path( args.output_file )
    output_path.parent.mkdir( parents=True, exist_ok=True )

    print( f"💾 Saving to {args.output_file}..." )
    prs.save( args.output_file )

    print( f"✅ Conversion completed! Generated {len( slides )} slides." )
    print( f"📁 Output: {args.output_file}" )
    return 0


if __name__ == '__main__':
    exit( main() )