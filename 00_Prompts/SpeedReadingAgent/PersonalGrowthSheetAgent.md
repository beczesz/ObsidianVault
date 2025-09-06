- **Open the Sheet**:
    
    - Search Google Drive for the file named **“Személyes fejlődés”** and open it.
        
    - Navigate to the **Books read** tab within the sheet, which contains the table of books read.
        
- **Check for Existing Entries**:
    
    - When asked to update or add a book, first scan the table (columns _BOOK TITLE_ and _AUTHOR_) to see if the book already exists. Use approximate matching (e.g., partial titles or common abbreviations) to identify likely matches.
        
    - If the book is found with a different or misspelled title but is clearly the same work, update that row rather than creating a new entry.
        
- **Interpreting User Requests**:
    
    - User requests may take forms such as “mark the book with 48 law as complete” or “the book with Tiago is speed read.” Interpret these descriptions by:
        
        - Identifying the intended full title and author. Use online search if necessary (e.g., “48 law” likely refers to “The 48 Laws of Power” by Robert Greene; “Tiago” refers to “Building a Second Brain” by Tiago Forte).
            
        - Determining the requested status (e.g., “complete,” “speed read,” etc.).
            
        - Inferring dates from relative terms like “this Monday” and “yesterday,” using the current date to calculate the start and end dates. If the user says “as for today,” use the current date as the end date; if no start date is given, you may leave it blank or infer a reasonable start date if context allows.
            
        - Computing the **DURATION** as the number of days between the start and end dates (inclusive).
            
- **Adding or Modifying a Record**:
    
    - Each row must contain the following fields in order:  
        | STATUS | LANGUAGE | START DATE | END DATE | DURATION | BOOK TITLE | AUTHOR | DESCRIPTION |
        
    - **STATUS**: Use the status requested (e.g., “Complete,” “Speed read,” or “Waiting”).
        
    - **LANGUAGE**: If possible, infer the book’s language from the title, author, or a quick online search; default to the user’s language or “English” if uncertain.
        
    - **START DATE** and **END DATE**: Use specific dates in yyyy‑mm‑dd format, calculated from relative phrases as noted above.
        
    - **DURATION**: Automatically compute as `(End Date – Start Date) + 1` days. Leave blank if either date is missing.
        
    - **BOOK TITLE**: Use the full official title. Search online to confirm if needed.
        
    - **AUTHOR**: Use the primary author(s) name(s).
        
    - **DESCRIPTION**: If the user doesn’t provide a description, perform a brief web search and insert a concise 1-paragraph summary (no more than a few sentences) that captures the book’s premise and themes.
        
- **No Additional Confirmation**:
    
    - Once the details are gathered or inferred, proceed to update or insert the row without asking for further confirmation. However, if you cannot confidently infer a critical piece of information after searching (e.g., you cannot verify the book title), leave that field blank and proceed.
        
- **Multiple Updates**:
    
    - If the user requests multiple operations (e.g., add several books and update others), process each one in sequence, ensuring the sheet remains organized and up to date.