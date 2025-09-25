#!/usr/bin/env python3
"""
Blog Post to Slide Notes Mapper
Maps sections from the GCP certification blog post to slide presenter notes
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple


class BlogToNotesMapper:
    """Maps blog post sections to slide presenter notes"""

    def __init__( self, blog_path: str, slides_path: str ):
        self.blog_path     = Path( blog_path )
        self.slides_path   = Path( slides_path )
        self.blog_content  = ""
        self.slides_data   = []
        self.note_mappings = {}

    def load_content( self ):
        """Load blog post and slides content"""
        if not self.blog_path.exists():
            raise FileNotFoundError( f"Blog post not found: {self.blog_path}" )
        if not self.slides_path.exists():
            raise FileNotFoundError( f"Slides file not found: {self.slides_path}" )

        with open( self.blog_path, 'r', encoding='utf-8' ) as f:
            self.blog_content = f.read()

        with open( self.slides_path, 'r', encoding='utf-8' ) as f:
            slides_content = f.read()

        self.slides_data = self._parse_slides( slides_content )

    def _parse_slides( self, content: str ) -> List[Dict]:
        """Parse slides content into structured data"""
        slides = []
        slide_blocks = content.split( '---' )

        for i, block in enumerate( slide_blocks ):
            block = block.strip()
            if not block:
                continue

            # Extract slide title
            title_match = re.search( r'##\s+Slide\s+\d+:\s*(.+)', block )
            if not title_match:
                # Handle non-numbered slides
                title_match = re.search( r'##\s+(.+)', block )

            title = title_match.group( 1 ).strip() if title_match else f"Slide {i}"

            # Extract bullet points and content
            bullets = re.findall( r'^\s*[-*]\s+(.+)', block, re.MULTILINE )

            slides.append({
                'number': i,
                'title': title,
                'bullets': bullets,
                'content': block
            })

        return slides

    def create_mappings( self ):
        """Create mappings between slides and blog sections"""
        # Define manual mappings based on content analysis
        self.note_mappings = {
            "Who Doesn't Love Studying Evenings and Weekends?": self._extract_section_1(),
            "The Brain Damage Problem": self._extract_section_2(),
            "Breathless Podcasts vs. Big Faceful of Book": self._extract_section_3(),
            "The Golden Trick": self._extract_section_4(),
            "The Cookie Cutter Process": self._extract_section_5(),
            "The Chapter Grind": self._extract_section_6(),
            "The Practice Exam Two-Step": self._extract_section_7(),
            "Hastily vs. Leisurely": self._extract_section_8(),
            "The Learning Equation": self._extract_section_9(),
            "Handy Little Hack": self._extract_section_10(),
            "The Friday Disaster": self._extract_section_11(),
            "Distribution Mismatch": self._extract_section_12(),
            "Actionable & Obvious Wisdom": self._extract_section_13(),
            "Mindless Task Learning": self._extract_section_14(),
            "Final Words": self._extract_section_15()
        }

    def _extract_section_1( self ):
        """Extract presenter notes for slide 1"""
        return """
**Context**: The frustration of mandatory certification prep
- Most people don't enjoy studying for certifications in their off hours
- Negative emotions create poor learning outcomes (educational psychology principle)
- Author's previous PMLE experience was a "cognitive nightmare" - cramming everything into 2 months
- This presentation shares lessons learned to make the process more sustainable

**Teaching Point**: Address the emotional barriers to learning first before diving into techniques
"""

    def _extract_section_2( self ):
        """Extract presenter notes for slide 2"""
        return """
**The Core Problem**: Cognitive overload after long work weeks
- 50-60 hour work weeks leave people mentally exhausted
- Best cognitive capacity is already consumed by day job
- Traditional study methods (reading books) don't work when you're brain-damaged
- Solution needed: low-friction information ingestion method

**Key Insight**: You need to work with your depleted cognitive state, not against it
"""

    def _extract_section_3( self ):
        """Extract presenter notes for slide 3"""
        return """
**The NotebookLM Discovery**: Audio content as the game-changer
- Traditional books felt dry and painful to process
- NotebookLM's AI-generated podcasts made content "relentlessly relatable"
- Could consume content during automatic activities: biking, gym, walks
- Information went down "like cold water on a hot day" - easy and refreshing

**Implementation**: Scraped chapter content and fed it to NotebookLM for podcast generation
"""

    def _extract_section_4( self ):
        """Extract presenter notes for slide 4"""
        return """
**The Engagement Hack**: Mocking leads to predicting leads to learning
- Started making fun of the AI hosts' predictable banter
- This led to predicting their next words (active engagement)
- By second listen, was answering questions before the AI provided answers
- "Ding, ding, ding!" - this was the breakthrough moment

**Psychology**: Humor and prediction engage the brain more than passive listening
"""

    def _extract_section_5( self ):
        """Extract presenter notes for slide 5"""
        return """
**The Manual Process**: Tedious but effective
- Hand-curated content through copy-paste operations
- "Digital hammer and chisel" - primitive but functional
- Wished it could be scripted but did manual work
- Baseline assessment: 60% without preparation (not bad!)
- Shared podcasts with others to amortize the effort

**Lesson**: Sometimes you have to do things manually before you can automate them
"""

    def _extract_section_6( self ):
        """Extract presenter notes for slide 6"""
        return """
**The Systematic Approach**: Outer and inner loops
- Outer loop: Process all 12 chapters (2 chapters per week)
- Inner loop per chapter:
  1. Scrape, prompt, and build chapter + Q&A podcasts
  2. Listen to chapter podcast once
  3. Review Q&A podcast twice with active listening
  4. Take chapter exam
  5. Review incorrect answers podcast twice with active listening

**Result**: Structured, repeatable process that builds knowledge systematically
"""

    def _extract_section_7( self ):
        """Extract presenter notes for slide 7"""
        return """
**Practice Exam Strategy**: Learn from failures
- Take practice exam first
- Screenshot all incorrect answers
- Build podcast focused on mistakes
- Listen to failure podcast twice actively
- Retake exam to confirm improvement
- Score progression: 80% → 95%

**Key Principle**: Turn failures into focused learning opportunities
"""

    def _extract_section_8( self ):
        """Extract presenter notes for slide 8"""
        return """
**Time Pressure vs. Relaxed Pace**: The difference is astounding
- Round 1 (PMLE): 2 months of painful cramming
- Round 2 (PCA): 4 months, relaxed pace (~1 chapter per week)
- The difference was "astounding" - second time was "actually easy"
- Emphasis: "It was easy!" (worth repeating)

**Takeaway**: Spreading learning over time reduces cognitive load dramatically
"""

    def _extract_section_9( self ):
        """Extract presenter notes for slide 9"""
        return """
**The Learning Formula**: L = F × I × T × (1/Duress)
- Learning = Frequency × Intensity × Time × (inverse of Duress)
- Maximize all positive variables, minimize stress
- Built automaticity through repeated exposure
- This automaticity became crucial during the actual exam

**Application**: Design your study approach to optimize this equation
"""

    def _extract_section_10( self ):
        """Extract presenter notes for slide 10"""
        return """
**Multiple Choice Strategy**: Beyond 50-50 odds
- Standard advice: eliminate 2 obviously bad choices
- But you're not flipping a coin - use reasoning
- Practice elimination skills from Day 1 of prep
- Build cognitive reps through repeated scenario handling

**Critical Point**: Practice elimination skills early, not just before the exam
"""

    def _extract_section_11( self ):
        """Extract presenter notes for slide 11"""
        return """
**Real-World Test**: When everything goes wrong
- Got only 5 hours of sleep night before exam
- Was "miserably tired" during the test
- Struggled to pay attention and stay awake
- Automaticity built through preparation carried him through

**Proof**: The learning system worked even under sub-optimal conditions
"""

    def _extract_section_12( self ):
        """Extract presenter notes for slide 12"""
        return """
**Content Distribution Mismatch**: Prep materials vs. actual exam
- Podcasts overemphasized database selection decisions
- Exam had more Kubernetes/GKE cluster scenarios than expected
- Apigee was mentioned on exam but never appeared in prep material
- Case studies were underrepresented in preparation

**Advice**: Seek additional GKE scenarios and understand Apigee basics
"""

    def _extract_section_13( self ):
        """Extract presenter notes for slide 13"""
        return """
**Core Wisdom**: Start now + practice elimination
- Two-word advice: "Start now" (obvious but crucial)
- Practice scenario-based question answering from beginning
- Always eliminate 2 bad choices first
- Combine your learning style with supplemental podcasts

**Meta-advice**: We all have different learning styles, but audio can supplement any approach
"""

    def _extract_section_14( self ):
        """Extract presenter notes for slide 14"""
        return """
**Multitasking Learning**: Use automatic physical tasks
- Commuting = podcast time
- Dishes, laundry, cleaning = learning opportunities
- Any "physically automatic" task can be paired with audio learning
- "Getting other things done" while building knowledge

**Efficiency**: Transform mindless tasks into learning sessions
"""

    def _extract_section_15( self ):
        """Extract presenter notes for slide 15"""
        return """
**Final Advice**: Learn from the author's mistake
- "Get a good night's sleep!" (unlike his exam day)
- This ties back to the Friday disaster story
- Proper rest is part of exam preparation
- Audience engagement: "What's your certification horror story?"

**Closure**: End with practical advice and audience interaction
"""

    def generate_notes_mapping( self ) -> Dict[str, str]:
        """Generate mapping of slide titles to presenter notes"""
        self.load_content()
        self.create_mappings()

        # Match slides to mappings
        result = {}
        for slide in self.slides_data:
            title = slide['title']
            # Find best matching key in mappings
            for mapping_key, notes in self.note_mappings.items():
                if mapping_key.lower() in title.lower() or title.lower() in mapping_key.lower():
                    result[title] = notes
                    break
            else:
                result[title] = f"**Slide**: {title}\n**Content**: {slide['bullets']}\n\n*Add presenter notes here*"

        return result

    def export_notes_file( self, output_path: str ):
        """Export mapped notes to a file"""
        mappings = self.generate_notes_mapping()

        with open( output_path, 'w', encoding='utf-8' ) as f:
            f.write( "# GCP Certification Prep - Presenter Notes\n\n" )
            f.write( "Generated from blog post content mapping\n\n" )
            f.write( "---\n\n" )

            for i, (title, notes) in enumerate( mappings.items(), 1 ):
                f.write( f"## Slide {i}: {title}\n\n" )
                f.write( f"{notes}\n\n" )
                f.write( "---\n\n" )

        print( f"✅ Presenter notes exported to: {output_path}" )


def main():
    """Main function for command line usage"""
    import argparse

    parser = argparse.ArgumentParser( description='Map blog post sections to slide presenter notes' )
    parser.add_argument( 'blog_post', help='Path to blog post markdown file' )
    parser.add_argument( 'slides_file', help='Path to slides markdown file' )
    parser.add_argument( 'output_file', help='Path for output presenter notes file' )

    args = parser.parse_args()

    mapper = BlogToNotesMapper( args.blog_post, args.slides_file )
    mapper.export_notes_file( args.output_file )


if __name__ == '__main__':
    main()