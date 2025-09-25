#!/usr/bin/env python3
"""
Master Markdown-to-PPTX Conversion Script
Unified interface for all tested conversion approaches
"""

import sys
import subprocess
import argparse
from pathlib import Path
import tempfile
from datetime import datetime


class ConversionMaster:
    """Master conversion coordinator for markdown-to-PPTX workflows"""

    def __init__( self ):
        self.project_root = Path( __file__ ).parent
        self.approaches   = {
            'pandoc-basic'    : self._pandoc_basic,
            'pandoc-enhanced' : self._pandoc_enhanced,
            'pandoc-with-notes': self._pandoc_with_notes,
            'python-md2pptx'  : self._python_md2pptx,
            'all-approaches'  : self._all_approaches
        }

    def convert( self, approach: str, input_file: str, output_file: str = None, **kwargs ):
        """Execute conversion using specified approach"""

        if approach not in self.approaches:
            self._print_error( f"Unknown approach: {approach}" )
            self._show_approaches()
            return False

        # Default output file based on approach
        if not output_file:
            input_path = Path( input_file )
            timestamp = datetime.now().strftime( "%Y%m%d_%H%M" )
            output_file = f"{input_path.stem}_{approach}_{timestamp}.pptx"

        print( f"🎯 Master Converter - {approach.title()} Approach" )
        print( f"{'='*50}" )
        print( f"📝 Input:  {input_file}" )
        print( f"📁 Output: {output_file}" )
        print( f"⏰ Started: {datetime.now().strftime('%H:%M:%S')}" )
        print()

        try:
            success = self.approaches[approach]( input_file, output_file, **kwargs )

            if success:
                self._show_results( output_file )

            return success

        except Exception as e:
            self._print_error( f"Conversion failed: {e}" )
            return False

    def _pandoc_basic( self, input_file: str, output_file: str, **kwargs ):
        """Basic Pandoc conversion"""
        cmd = [
            "pandoc",
            input_file,
            "-t", "pptx",
            "-o", output_file
        ]

        return self._run_command( cmd, "Basic Pandoc conversion" )

    def _pandoc_enhanced( self, input_file: str, output_file: str, **kwargs ):
        """Enhanced Pandoc conversion with metadata"""
        cmd = [
            "pandoc",
            input_file,
            "-t", "pptx",
            "--slide-level=2",
            "--metadata", "title=GCP Certification Prep - Enhanced",
            "-o", output_file
        ]

        return self._run_command( cmd, "Enhanced Pandoc conversion" )

    def _pandoc_with_notes( self, input_file: str, output_file: str, blog_file: str = None, **kwargs ):
        """Pandoc conversion with presenter notes from blog post"""

        # Default blog file
        if not blog_file:
            blog_file = str( self.project_root / "rnd" / "gcp-cloud-certification-blog-post.md" )

        # Run the enhanced conversion script
        script_path = self.project_root / "04-pandoc-universal" / "scripts" / "convert_with_notes.py"

        cmd = [
            "python",
            str( script_path ),
            "--slides", input_file,
            "--blog", blog_file,
            "--output-dir", str( Path( output_file ).parent )
        ]

        if self._run_command( cmd, "Pandoc with presenter notes" ):
            # Move the generated file to the desired output name
            generated_file = Path( output_file ).parent / "gcp-slides-with-notes.pptx"
            if generated_file.exists():
                generated_file.rename( output_file )
                return True

        return False

    def _python_md2pptx( self, input_file: str, output_file: str, **kwargs ):
        """Python md2pptx conversion"""
        script_path = self.project_root / "03-md2pptx-python" / "scripts" / "convert.py"
        venv_path = self.project_root / "03-md2pptx-python" / ".venv" / "bin" / "python"

        # Use virtual environment if available
        python_cmd = str( venv_path ) if venv_path.exists() else "python"

        cmd = [
            python_cmd,
            str( script_path ),
            input_file,
            output_file
        ]

        return self._run_command( cmd, "Python md2pptx conversion" )

    def _all_approaches( self, input_file: str, output_file: str, **kwargs ):
        """Run all working approaches for comparison"""
        output_path = Path( output_file )
        output_dir = output_path.parent
        base_name = output_path.stem

        approaches = [
            ( 'pandoc-basic', f"{base_name}_pandoc_basic.pptx" ),
            ( 'pandoc-enhanced', f"{base_name}_pandoc_enhanced.pptx" ),
            ( 'pandoc-with-notes', f"{base_name}_pandoc_notes.pptx" ),
            ( 'python-md2pptx', f"{base_name}_python.pptx" )
        ]

        results = []
        for approach, filename in approaches:
            output_file_path = output_dir / filename
            print( f"\n🔄 Running {approach}..." )

            success = self.approaches[approach]( input_file, str( output_file_path ), **kwargs )
            results.append( ( approach, filename, success ) )

        # Summary
        print( f"\n📊 BATCH CONVERSION SUMMARY" )
        print( f"{'='*40}" )

        for approach, filename, success in results:
            status = "✅ SUCCESS" if success else "❌ FAILED"
            print( f"{status:12} {approach:20} → {filename}" )

        return all( success for _, _, success in results )

    def _run_command( self, cmd: list, description: str ):
        """Run subprocess command with error handling"""
        print( f"🔧 {description}..." )

        try:
            result = subprocess.run( cmd, check=True, capture_output=True, text=True )
            print( f"✅ {description} completed" )
            return True

        except subprocess.CalledProcessError as e:
            self._print_error( f"{description} failed: {e.stderr}" )
            return False

        except FileNotFoundError:
            self._print_error( f"Command not found: {cmd[0]}" )
            return False

    def _show_results( self, output_file: str ):
        """Show conversion results"""
        output_path = Path( output_file )

        if output_path.exists():
            file_size = output_path.stat().st_size / 1024
            print( f"\n🎉 Conversion completed successfully!" )
            print( f"📁 Output file: {output_file}" )
            print( f"📏 File size: {file_size:.1f} KB" )
            print( f"⏰ Completed: {datetime.now().strftime('%H:%M:%S')}" )
        else:
            self._print_error( f"Output file not found: {output_file}" )

    def _print_error( self, message: str ):
        """Print error message"""
        print( f"❌ ERROR: {message}" )

    def _show_approaches( self ):
        """Show available approaches"""
        print( f"\n📋 Available conversion approaches:" )
        print( f"  pandoc-basic      - Basic Pandoc conversion (44KB, fast)" )
        print( f"  pandoc-enhanced   - Enhanced Pandoc with metadata (44KB, fast)" )
        print( f"  pandoc-with-notes - Pandoc with presenter notes (70KB, rich)" )
        print( f"  python-md2pptx    - Python conversion (42KB, fastest)" )
        print( f"  all-approaches    - Run all approaches for comparison" )

    def show_status( self ):
        """Show system status and requirements"""
        print( f"🔍 System Status Check" )
        print( f"{'='*30}" )

        # Check dependencies
        dependencies = [
            ( "pandoc", ["pandoc", "--version"] ),
            ( "python", ["python", "--version"] ),
        ]

        for name, cmd in dependencies:
            try:
                result = subprocess.run( cmd, check=True, capture_output=True, text=True )
                version = result.stdout.split('\n')[0]
                print( f"✅ {name:10} {version}" )
            except:
                print( f"❌ {name:10} Not available" )

        # Check project structure
        print( f"\n📁 Project Structure:" )

        key_paths = [
            ( "Pandoc scripts", "04-pandoc-universal/scripts/convert_with_notes.py" ),
            ( "Python scripts", "03-md2pptx-python/scripts/convert.py" ),
            ( "Blog post", "../rnd/gcp-cloud-certification-blog-post.md" ),
            ( "Test slides", "shared/input/gcp-cert-prep-slides-v2.md" )
        ]

        for name, path in key_paths:
            full_path = self.project_root / path
            status = "✅ Found" if full_path.exists() else "❌ Missing"
            print( f"{status} {name:15} {path}" )


def main():
    """Main command line interface"""
    parser = argparse.ArgumentParser(
        description='Master markdown-to-PPTX converter',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s input.md --approach pandoc-basic
  %(prog)s input.md --approach pandoc-with-notes --output presentation.pptx
  %(prog)s input.md --approach python-md2pptx
  %(prog)s input.md --approach all-approaches --output batch_comparison.pptx
  %(prog)s --status
        """
    )

    parser.add_argument( 'input_file', nargs='?', help='Input markdown file' )
    parser.add_argument( '--approach', '-a',
                        choices=['pandoc-basic', 'pandoc-enhanced', 'pandoc-with-notes', 'python-md2pptx', 'all-approaches'],
                        default='pandoc-enhanced',
                        help='Conversion approach to use (default: pandoc-enhanced)' )
    parser.add_argument( '--output', '-o', help='Output PPTX file path' )
    parser.add_argument( '--blog-file', help='Blog post file for presenter notes (pandoc-with-notes only)' )
    parser.add_argument( '--status', action='store_true', help='Show system status and exit' )

    args = parser.parse_args()

    converter = ConversionMaster()

    if args.status:
        converter.show_status()
        return 0

    if not args.input_file:
        parser.print_help()
        return 1

    # Check if input file exists
    if not Path( args.input_file ).exists():
        converter._print_error( f"Input file not found: {args.input_file}" )
        return 1

    # Run conversion
    success = converter.convert(
        approach=args.approach,
        input_file=args.input_file,
        output_file=args.output,
        blog_file=args.blog_file
    )

    return 0 if success else 1


if __name__ == '__main__':
    exit( main() )