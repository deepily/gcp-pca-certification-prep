#!/usr/bin/env python3
"""
Create a PowerPoint reference template with Arial/Helvetica Neue fonts
Modifies the default Pandoc reference to use preferred fonts
"""

import sys
from pathlib import Path
from pptx import Presentation
from pptx.enum.text import MSO_ANCHOR


def modify_font_template( input_path: str, output_path: str, preferred_fonts: list ):
    """Modify PowerPoint template to use preferred fonts"""

    print( f"📝 Loading template: {input_path}" )
    prs = Presentation( input_path )

    # Font priority: try Helvetica Neue first, fallback to Arial
    font_name = preferred_fonts[0]  # Start with first preference

    print( f"🎨 Setting fonts to: {font_name}" )

    # Modify slide layouts
    layouts_modified = 0
    for layout in prs.slide_layouts:
        try:
            # Modify placeholders in each layout
            for placeholder in layout.placeholders:
                if hasattr( placeholder, 'text_frame' ) and placeholder.text_frame:
                    # Set default paragraph font
                    for paragraph in placeholder.text_frame.paragraphs:
                        if paragraph.font:
                            paragraph.font.name = font_name

                    # Set text frame default font
                    if hasattr( placeholder.text_frame, 'auto_size' ):
                        # Apply font to the text frame's default character formatting
                        placeholder.text_frame.word_wrap = True

            layouts_modified += 1

        except Exception as e:
            print( f"⚠️  Warning: Could not modify layout {layout.name}: {e}" )
            continue

    # Modify slide masters
    masters_modified = 0
    for slide_master in prs.slide_masters:
        try:
            # Modify placeholders in slide master
            for placeholder in slide_master.placeholders:
                if hasattr( placeholder, 'text_frame' ) and placeholder.text_frame:
                    for paragraph in placeholder.text_frame.paragraphs:
                        if paragraph.font:
                            paragraph.font.name = font_name

            masters_modified += 1

        except Exception as e:
            print( f"⚠️  Warning: Could not modify slide master: {e}" )
            continue

    # Save the modified template
    print( f"💾 Saving font template: {output_path}" )
    prs.save( output_path )

    print( f"✅ Font template created successfully!" )
    print( f"📊 Modified {layouts_modified} layouts and {masters_modified} slide masters" )
    print( f"🎯 Font set to: {font_name}" )

    return True


def create_multiple_font_templates():
    """Create templates for different font preferences"""

    base_path = Path( "templates" )
    input_file = base_path / "default-reference.pptx"

    # Font preferences in priority order
    font_options = [
        ( ["Helvetica Neue", "Arial", "Helvetica"], "helvetica-neue-reference.pptx" ),
        ( ["Arial", "Helvetica Neue"], "arial-reference.pptx" ),
        ( ["Calibri", "Arial"], "calibri-reference.pptx" )  # Backup modern option
    ]

    templates_created = []

    for fonts, filename in font_options:
        output_file = base_path / filename

        try:
            modify_font_template( str( input_file ), str( output_file ), fonts )
            templates_created.append( filename )

        except Exception as e:
            print( f"❌ Failed to create {filename}: {e}" )
            continue

    print( f"\n🎉 Created {len( templates_created )} font templates:" )
    for template in templates_created:
        template_path = base_path / template
        file_size = template_path.stat().st_size / 1024
        print( f"  ✅ {template} ({file_size:.1f} KB)" )

    # Set the primary template (try Helvetica Neue first, fallback to Arial)
    primary_template = base_path / "custom-reference.pptx"
    if (base_path / "helvetica-neue-reference.pptx").exists():
        (base_path / "helvetica-neue-reference.pptx").rename( primary_template )
        print( f"🎯 Primary template: Helvetica Neue" )
    elif (base_path / "arial-reference.pptx").exists():
        (base_path / "arial-reference.pptx").rename( primary_template )
        print( f"🎯 Primary template: Arial" )

    return len( templates_created ) > 0


def main():
    """Main function"""
    print( "🎨 Creating PowerPoint Font Templates" )
    print( "====================================" )

    # Check if input template exists
    input_template = Path( "templates/default-reference.pptx" )
    if not input_template.exists():
        print( f"❌ Default template not found: {input_template}" )
        print( "   Run: pandoc -o templates/default-reference.pptx --print-default-data-file reference.pptx" )
        return 1

    # Create font templates
    if create_multiple_font_templates():
        print( f"\n✅ Font template creation completed!" )
        print( f"📁 Templates available in: templates/" )
        print( f"🚀 Ready to use with Pandoc --reference-doc option" )
        return 0
    else:
        print( f"\n❌ Failed to create font templates" )
        return 1


if __name__ == '__main__':
    exit( main() )