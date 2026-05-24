# Speed Reader Plugin

**Version:** 0.7.0
**Author:** Szabolcs (exarlabs@gmail.com)
**License:** MIT

AI-powered speed-reading system that transforms books, podcasts, and articles into comprehensive, structured notes for your Obsidian vault using the PARA organizational method.

## Overview

The Speed Reader plugin uses a multi-agent architecture to process written and audio content into detailed, well-organized notes that integrate seamlessly into your knowledge management system.

### What It Does

- **Processes multiple content types**: Books (PDFs/ePubs), podcasts (transcripts), web articles, or title-only research
- **Deep analysis**: Chapter-by-chapter breakdown with guiding questions, key ideas, thesis extraction, and critical commentary
- **Context research**: Automatically gathers author biographies, historical context, reception history, and comparable works
- **Structured output**: Generates notes following PARA folder structure with proper YAML frontmatter and Obsidian wikilinks
- **Google Drive sync**: Optional upload to maintain cloud backup of your knowledge vault

## Architecture

The plugin uses a sophisticated multi-agent system:

### Main Components

1. **Speed-Reader Skill** (Orchestrator)
   - Coordinates the entire workflow
   - Classifies input and prepares templates
   - Assembles final outputs from sub-agents
   - Handles formatting and PARA organization

2. **Context-Researcher Agent** (Sub-agent)
   - Researches books, authors, and works on the web
   - Gathers: author bio, reception, historical context, comparable works
   - Marks uncertain information appropriately
   - Provides citations for all research

3. **Chapter-Analyzer Agent** (Sub-agent)
   - Performs deep chapter-by-chapter analysis
   - Generates: guiding questions, key ideas (½-2 pages per chapter), thesis statements
   - Provides: extended commentary, skeptical challenges, applications
   - Extracts 5-10 key quotes with page numbers

4. **Upload Command**
   - Syncs generated notes to Google Drive
   - Maintains PARA folder structure in the cloud
   - Handles multiple file types and overwrites

## Installation

1. Install the plugin file: `speed-reader.plugin`
2. The plugin will be available in your Claude Cowork session
3. Optional: Connect the Google Drive connector for upload functionality

## Usage

### Basic Usage

Simply describe what you want to process:

```
"Summarize the book Influence by Robert Cialdini"
```

```
"Analyze this PDF for my Idea Vault"
[attach PDF file]
```

```
"Create speed-reading notes for this podcast transcript"
[attach transcript]
```

### Input Types Supported

| Input Type | Example | What Happens |
|-----------|---------|--------------|
| **Full PDF/ePub** | Upload a book file | Deep chapter-by-chapter analysis with quotes |
| **Title only** | "Atomic Habits by James Clear" | Web research for context and summary |
| **Article URL** | https://example.com/article | Fetches and analyzes the article |
| **Podcast transcript** | Upload .txt transcript | Analyzes by timestamps/segments |

### Triggering the Skill

The speed-reader skill activates when you:
- Mention "speed-read", "summarize", "analyze", or "take notes"
- Reference your "Idea Vault" or "Obsidian vault"
- Mention "PARA", "atomic notes", or "contrast notes"
- Provide a PDF/ePub with instructions to process it

### Using the Upload Command

After generating notes, sync them to Google Drive:

```
/upload
```

You'll be prompted to specify which files to upload. The command will:
1. Ask you which files to upload
2. Show you the planned folder structure
3. Create folders in Google Drive as needed
4. Upload files maintaining PARA organization
5. Report success/failure for each file

**Note**: You must have the Google Drive connector connected for upload to work.

## Output Structure

### PARA Organization

All generated notes follow the PARA (Projects, Areas, Resources, Archives) method:

```
Idea Vault/
├── 03_Resources/
│   ├── 02_Books/
│   │   ├── <Author - Title>/          # Individual book folders
│   │   │   ├── Title_Author_Year.md   # Summary note
│   │   │   └── Title_Author.pdf       # Source file
│   │   ├── Atomic_Ideas/              # Concept notes
│   │   └── Contrasts/                 # Comparison notes
│   ├── 03_Podcasts/
│   └── 04_Articles/
```

### Note Contents

Each generated note includes:

**Metadata Section**:
- YAML frontmatter with title, type, author, year, tags, confidence level
- Master Prompt version
- 1-line thesis statement

**Context Dossier**:
- Author biography and credentials
- Historical and cultural context
- Genre and tradition placement
- Reception and influence
- Comparable works
- Target audience

**Main Content**:
- Abstract (≤ 300 words)
- Chapter-by-chapter analysis (for full-text)
  - Guiding question
  - Expanded key ideas (½-2 pages)
  - Thesis statements
  - Extended commentary with cross-references
  - Skeptical challenges
  - Applications and implications

**Supplementary Material**:
- 5-10 key quotes with page numbers
- 5-10 relevant tags
- Suggested atomic notes (concepts worth separate notes)
- Suggested contrast notes (comparative analyses)
- Citations (for web-researched content)

## Features

### Quality Standards

- **No hallucinations**: All information is extracted from sources or marked as [Inference]
- **Citation integrity**: Web research includes source citations
- **Fair use**: Quotes are kept short and properly attributed
- **Uncertainty marking**: Ambiguous information flagged with [Uncertain]
- **No fabrication**: Page numbers never invented; uses "Ch. X" if unavailable

### Obsidian Integration

- Uses `[[wikilinks]]` for cross-references
- YAML frontmatter compatible with Dataview queries
- Maintains proper folder structure for graph view
- Tags for filtering and organization

### Multi-Agent Benefits

- **Parallel processing**: Context research and chapter analysis run simultaneously when possible
- **Specialization**: Each agent focuses on its expertise (research vs. analysis)
- **Quality**: Dedicated agents produce deeper, more thorough outputs
- **Modularity**: Agents can be improved or replaced independently

## Configuration

### File Naming Conventions

The plugin uses these naming patterns:

| Type | Pattern | Example |
|------|---------|---------|
| Book | `Title_Author_Year.md` | `Influence_Robert_B_Cialdini_1984.md` |
| Podcast | `Show_EpNNN_Title_YYYY-MM-DD.md` | `Huberman_Ep042_Sleep_2023-03-15.md` |
| Article | `Source_Title_Author_Year.md` | `HBR_Leading_Change_Kotter_1995.md` |
| Atomic | `Concept_Name.md` | `Scarcity_Mindset.md` |
| Contrast | `A_vs_B_on_Theme.md` | `Peterson_vs_Dostoevsky_on_Suffering.md` |

**Collision handling**: Files never overwrite existing ones; version suffixes (-v2, -v3) are appended if needed.

### Customizing the Vault Location

By default, the plugin uses the folder structure specified in:
- `skills/speed-reader/references/vault-structure.md`

To customize your vault location or folder names, edit this reference file.

### Google Drive Setup

1. Connect the Google Drive MCP connector in Claude Cowork
2. The plugin will automatically detect the connection
3. Use `/upload` command or request "and upload it" when processing content
4. Files sync to `/Idea Vault/` in your Google Drive maintaining PARA structure

## Examples

### Example 1: Full Book Analysis

```
User: "Process this PDF of Thinking, Fast and Slow for my Idea Vault"
[attaches PDF]

Speed-Reader:
1. Launches context-researcher → gathers Kahneman bio, book reception, comparable works
2. Launches chapter-analyzer → processes all chapters with deep analysis
3. Assembles complete note with:
   - Context dossier
   - Abstract and thesis
   - 25 chapters analyzed (½-2 pages each)
   - 8 key quotes with page numbers
   - 6 atomic note suggestions (e.g., "System 1 vs System 2", "Anchoring Bias")
   - 3 contrast note suggestions (e.g., "Kahneman_vs_Ariely_on_Rationality")
4. Saves to: /03_Resources/02_Books/Daniel Kahneman - Thinking, Fast and Slow/
```

### Example 2: Title-Only Research

```
User: "Speed-read The Lean Startup by Eric Ries"

Speed-Reader:
1. Launches context-researcher → finds author bio, book summary, reception online
2. Skips chapter-analyzer (no full text)
3. Searches web for TOC and chapter summaries
4. Assembles note with:
   - Full context dossier
   - Best-available summary from web sources
   - Estimated chapter topics
   - [Uncertain] flags where sources disagree
   - All web sources cited
5. Saves to: /03_Resources/02_Books/Eric Ries - The Lean Startup/
```

### Example 3: With Upload

```
User: "Analyze this article and upload it to Google Drive"
[attaches article PDF]

Speed-Reader:
1. Processes article (context research + section analysis)
2. Detects upload request
3. Checks Google Drive connection
4. Creates note locally
5. Uploads to: /Idea Vault/03_Resources/04_Articles/ in Google Drive
6. Reports: "✓ Uploaded to Google Drive: article-name.md"
```

## Troubleshooting

### "Google Drive connector not available"

**Solution**: Connect the Google Drive MCP connector:
1. Say "connect Google Drive" or "add Google Drive connector"
2. Follow the authorization flow
3. Retry the upload

### "File already exists in Google Drive"

**Behavior**: The plugin will overwrite the existing file (as per configuration)
**To change**: Edit `commands/upload.md` to modify overwrite behavior

### "Chapter analysis seems shallow"

**Possible causes**:
- The book PDF might have extraction issues
- The chapter might genuinely be short
**Solution**: Verify the PDF is readable; check if specific chapters are problematic

### "No page numbers in quotes"

**Expected behavior**: If page numbers aren't available in the source, the plugin uses "Ch. X" instead
**This is intentional**: The plugin never fabricates page numbers

## Advanced Usage

### Customizing Templates

Edit `skills/speed-reader/references/templates.md` to customize:
- Book summary template
- Podcast summary template
- Article summary template
- Atomic note stub format
- Contrast note stub format

### Customizing YAML Frontmatter

Edit `skills/speed-reader/references/frontmatter-spec.md` to modify:
- Required fields
- Optional fields
- Field formats
- Status values
- Confidence levels

### Adjusting Analysis Depth

The chapter-analyzer agent is configured for "comprehensive" analysis (½-2 pages per chapter).

To adjust, edit `agents/chapter-analyzer.md` and modify the length guidance in the "Expanded Answer & Key Ideas" section.

## Version History

### v0.7.0 (Current)
- Multi-agent architecture with context-researcher and chapter-analyzer
- Comprehensive chapter analysis (½-2 pages per chapter)
- Google Drive upload integration
- PARA folder structure enforcement
- Uncertainty marking and citation requirements
- Fair use quote extraction

## Support

For issues, questions, or feature requests:
- Email: exarlabs@gmail.com
- Check plugin documentation in `skills/` and `agents/` directories
- Review reference files in `skills/speed-reader/references/`

## License

MIT License - See plugin.json for details

---

**Happy speed-reading!** 📚✨
