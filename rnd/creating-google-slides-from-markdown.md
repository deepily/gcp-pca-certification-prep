# Automated markdown to Google Slides conversion with AI integration

Based on comprehensive research across multiple repositories, frameworks, and implementation approaches, I've identified proven automated workflows for converting markdown-formatted outlines to Google Slides presentations, with options for AI-generated image integration. The landscape reveals three primary conversion strategies: direct PPTX export (which Google Slides imports natively), intermediate format workflows, and API-based direct integration.

## Production-ready solutions with PPTX export capability

The most reliable path to Google Slides involves generating PPTX files that import cleanly into the platform. **Marp CLI** emerges as the most mature solution with 9,600 GitHub stars across its ecosystem. The tool provides direct PPTX export via a simple command: `marp slides.md --pptx` or `marp slides.md -o output.pptx`. The Marp team maintains multiple repositories including the CLI tool (github.com/marp-team/marp-cli), core engine (marp-core), VS Code extension, and the Marpit framework. It supports Docker deployment (`marpteam/marp-cli`), GitHub Actions integration, and batch processing with custom CSS themes. The PPTX output consists of pre-rendered high-resolution images (2x scale factor by default) with preserved presenter notes, though an experimental `--pptx-editable` flag enables text editing via LibreOffice.

**Slidev** represents the modern alternative with 40,300 stars on GitHub (github.com/slidevjs/slidev), built on Vue.js and Vite. Beyond PPTX export via `slidev export --format pptx`, it offers live coding with Monaco Editor, interactive Vue components, recording capabilities, and drawing features. Installation is straightforward with `npm init slidev@latest`, and the tool provides both CLI and browser-based export interfaces. The PPTX output preserves presenter notes and animation steps when using the `--with-clicks` option.

For Python developers, **md2pptx by Martin Packer** (github.com/MartinPacker/md2pptx) stands out as the most comprehensive implementation. This production-tested solution uses python-pptx as its foundation, supporting PowerPoint templates, table of contents generation, task lists, glossary slides, and Critic Markup for review workflows. Usage follows a Unix pipeline pattern: `python3 md2pptx output.pptx < input.markdown`. The tool handles complex markdown including headers, bullets, code blocks, images, tables, and slide notes.

## Intermediate format workflows and conversion pipelines

**Pandoc** offers the most flexible universal conversion approach with native editable PPTX output. Unlike image-based exports, Pandoc generates PowerPoint files with actual text and shapes: `pandoc slides.md -t pptx -o presentation.pptx`. The `--reference-doc=template.pptx` option enables custom layouts and consistent branding. With 39,200 stars on GitHub (github.com/jgm/pandoc), it supports over 50 input/output formats, LaTeX math rendering, and automatic bibliographies.

The **reveal.js ecosystem** provides a different intermediate approach through HTML presentations. The reveal-md wrapper (github.com/webpro/reveal-md) generates web-based slideshows with `reveal-md slides.md --static _site`, which can be converted to PDF via DeckTape and then imported to Google Slides. While indirect, this workflow preserves the rich interactivity of web presentations.

For direct Google Slides integration, **md2googleslides** (github.com/googleworkspace/md2googleslides) exists as an official Google Workspace tool but suffers from authentication complexity. It supports CommonMark, GitHub Flavored Markdown, tables, YouTube videos, math expressions, and two-column layouts. However, OAuth setup issues limit its practical deployment.

## Python-pptx ecosystem and implementation patterns

The **python-pptx library** (github.com/scanny/python-pptx) serves as the foundation for all Python-based converters. This mature library by Steve Canny enables cross-platform PPTX generation without PowerPoint installation, supporting text formatting, images, tables, charts, shapes, and templates. A minimal implementation demonstrates the simplicity:

```python
from pptx import Presentation
from pptx.util import Inches, Pt

prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[1])
title = slide.shapes.title
title.text = "Generated from Markdown"
prs.save('presentation.pptx')
```

Additional Python tools include **mdtopptx** (available via PyPI), which provides a clean two-function API for parsing markdown and creating presentations. The **pptx2md** tool (github.com/ssine/pptx2md) enables reverse conversion for understanding PPTX structure and creating markdown templates, supporting fuzzy title hierarchy detection, image extraction, and table handling including merged cells.

## AI-powered image generation integration

**Presenton** (github.com/presenton/presenton) leads the open-source landscape for AI-integrated presentations. It supports multiple image providers including DALL-E 3, Gemini Flash, Pexels, and Pixabay through a bring-your-own-key model. The tool offers Docker deployment, REST API endpoints, custom HTML templates, and export to both PPTX and PDF. A typical API call generates a complete presentation: `curl -X POST http://localhost:5000/api/v1/ppt/presentation/generate -d '{"prompt": "Machine Learning Overview", "n_slides": 5}'`.

**SlideDeck AI** (github.com/barun-saha/slide-deck-ai) implements structured JSON-based content generation with keyword extraction for contextual image search. It supports multiple LLMs including Mistral NeMo, Gemini Flash, and GPT-4o, with offline capabilities via Ollama integration.

The **OpenAI Cookbook** provides a complete implementation example (cookbook.openai.com/examples/creating_slides_with_assistants_api_and_dall_e3) demonstrating the integration of Assistants API for content generation, DALL-E 3 for title images, and Code Interpreter for data visualization, all assembled using python-pptx templates.

For batch processing, **ComfyUI workflows** enable efficient generation of multiple images from prompt lists with automated upscaling and post-processing. The architecture follows a pipeline pattern: Content → Keyword Extraction → Image Generation → Layout Assembly.

## Complete GitHub repositories with end-to-end implementations

Several repositories demonstrate complete markdown-to-presentation pipelines. The **ENISHI Blog implementation** (enishiblog.org/post-4612) provides production-ready code handling Marp markdown format with special code block processing. The implementation splits slides on '---' delimiters, processes bullet points, and handles code blocks with appropriate formatting.

**QuikSlide** (github.com/EdwardJXLi/QuikSlide) showcases an academic approach with speech-to-text input processing, NLTK-based text summarization, and Google Slides API integration. **SlideAI** (github.com/siddhesh-desai/SlideAI) implements a Google Apps Script solution using OpenAI API for content generation and Bing API for contextual image search.

## Recommended workflow for automated conversion

For maximum automation and Google Slides compatibility, the optimal workflow combines Marp CLI for conversion with optional AI image generation. First, install Marp globally: `npm install -g @marp-team/marp-cli`. For basic conversion, execute `marp slides.md --pptx -o presentation.pptx`. Add custom theming with `marp slides.md --pptx --theme custom.css -o branded.pptx`. Enable watch mode for continuous development: `marp --watch slides.md --pptx`.

For CI/CD integration, deploy via GitHub Actions:

```yaml
name: Generate Presentations
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Marp Build
        uses: docker://marpteam/marp-cli:latest
        with:
          args: slides.md --pptx -o output.pptx
```

To integrate AI-generated images, extend the workflow with keyword extraction from markdown headers and content, generate contextual prompts maintaining visual consistency, batch process images via Stable Diffusion or DALL-E APIs, and insert images into slides before PPTX generation.

## Practical implementation considerations

The choice between solutions depends on specific requirements. **Marp** excels for straightforward markdown-to-PPTX conversion with strong automation support. **Slidev** suits teams preferring modern web development workflows with interactive features. **Pandoc** provides maximum flexibility for complex document transformations with editable output. **Python-based solutions** offer the most customization potential for specialized requirements.

For AI image integration, consider using Presenton for comprehensive out-of-box functionality, implementing custom pipelines with ComfyUI for cost-effective batch processing, or leveraging OpenAI APIs for high-quality results with simple integration. Budget-conscious implementations should explore Pollinations.ai for free image generation, local Stable Diffusion models via Ollama, or hybrid approaches mixing AI-generated and stock images.

All recommended solutions generate standard PPTX files that import cleanly into Google Slides, preserving text content, basic formatting, images, tables, and presenter notes. While some visual adjustments may be needed post-import, the automation significantly reduces manual presentation creation time while maintaining professional quality output.