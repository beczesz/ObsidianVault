---
name: upload
description: Upload speed-reader generated files to Google Drive maintaining PARA folder structure
id: bd69635f-e9d4-4918-8b1c-e9b917c10a6b
index_schema_version: 1
---

# Upload Command

Upload speed-reader output files to Google Drive in the appropriate PARA folder structure.

## Prerequisites

**CRITICAL**: Check if Google Drive MCP connector is available:
1. Look for Google Drive tools in your available tools
2. If not available, inform the user:
   ```
   To upload to Google Drive, you need to connect the Google Drive connector first.
   Would you like me to help you set that up?
   ```
3. Only proceed if Google Drive tools are accessible

## Step 1: Identify Files to Upload

Ask the user which files they want to upload. Provide options:

**Ask the user**:
> Which files would you like to upload to Google Drive?
>
> Please provide:
> - Specific file names or paths, OR
> - "all recent" for all files from the last speed-reader session, OR
> - "current directory" for all markdown files in the current folder

**Wait for user response** before proceeding.

## Step 2: Validate Files

For each file the user specifies:
1. Check if the file exists using Read tool
2. Read the YAML frontmatter to determine:
   - File type (book, podcast, article, atomic, contrast)
   - Title and author (for folder naming)
   - Any associated files mentioned in `file_refs`
3. Build a list of files to upload with their metadata

Example:
```
Found files to upload:
- Influence_Robert_B_Cialdini_1984.md (type: book, author: Robert B. Cialdini)
- Influence_Robert_B_Cialdini.pdf (source file)
```

## Step 3: Determine Target Folders

Map each file to its Google Drive destination based on the PARA structure:

| File Type | Google Drive Path |
|-----------|------------------|
| Book | `/Idea Vault/03_Resources/02_Books/<Author - Title>/` |
| Podcast | `/Idea Vault/03_Resources/03_Podcasts/` |
| Article | `/Idea Vault/03_Resources/04_Articles/` |
| Atomic Idea | `/Idea Vault/03_Resources/02_Books/Atomic_Ideas/` |
| Contrast | `/Idea Vault/03_Resources/02_Books/Contrasts/` |

**For books**: Create a subfolder named `<Author - Title>` (e.g., "Robert B. Cialdini - Influence")

Show the user the planned structure:
```
Upload plan:
✓ Influence_Robert_B_Cialdini_1984.md
  → /Idea Vault/03_Resources/02_Books/Robert B. Cialdini - Influence/

✓ Influence_Robert_B_Cialdini.pdf
  → /Idea Vault/03_Resources/02_Books/Robert B. Cialdini - Influence/
```

## Step 4: Create Google Drive Folders

For each unique target folder:
1. Check if the folder exists in Google Drive (use appropriate Google Drive tool)
2. If it doesn't exist, create it
3. Ensure the full PARA path is created (create parent folders if needed)

**Handle errors gracefully**:
- If folder creation fails, report to user and ask if they want to:
  - Skip this file
  - Try a different folder name
  - Create the folder manually and retry

## Step 5: Upload Files

For each file in the upload list:
1. Read the file content (using Read tool)
2. Upload to the target Google Drive folder (use appropriate Google Drive tool)
3. **Overwrite if file exists** (as per user preference)
4. Track success/failure for each upload

**Progress reporting**:
```
Uploading files...
✓ Uploaded: Influence_Robert_B_Cialdini_1984.md
✓ Uploaded: Influence_Robert_B_Cialdini.pdf
```

## Step 6: Report Results

Provide a summary to the user:

```
Upload complete!

Uploaded 2 files to Google Drive:

📁 /Idea Vault/03_Resources/02_Books/Robert B. Cialdini - Influence/
  ✓ Influence_Robert_B_Cialdini_1984.md
  ✓ Influence_Robert_B_Cialdini.pdf

All files synced to your Idea Vault in Google Drive.
```

**If any files failed**:
```
Upload completed with some issues:

✓ Successfully uploaded: 1 file
✗ Failed: 1 file
  - Influence_Robert_B_Cialdini.pdf (Error: File too large)

Please check the failed files and try again.
```

## Error Handling

**Google Drive not connected**:
> To upload files, you need to connect the Google Drive connector. I can guide you through the setup if you'd like.

**File not found**:
> I couldn't find the file "[filename]". Please check the file name and path, or provide a different file.

**Folder creation fails**:
> I couldn't create the folder "/path/to/folder" in Google Drive. Would you like to:
> 1. Try a different folder name
> 2. Create the folder manually and I'll upload to it
> 3. Skip this file

**Upload fails**:
> Failed to upload "[filename]": [error message]
> Would you like to retry?

**No files specified**:
> I need to know which files to upload. Please provide file names or paths, or say "all recent" to upload files from your last speed-reader session.

## Security & Safety

- Never upload files outside the PARA structure without explicit user confirmation
- Always show the upload plan before executing
- Never delete local files after upload (keep both copies)
- Respect Google Drive permissions and quotas
- If uncertain about any file operation, ask the user first

## Tips for Users

After the upload completes, remind the user:

> **Tip**: Your files are now in Google Drive under your Idea Vault. If you have Google Drive desktop sync enabled, they'll also appear in your local Obsidian vault automatically.
>
> Run `/upload` anytime to sync more speed-reader outputs!
