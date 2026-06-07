---
name: daily-yahoo-inbox-digest
description: Generate a digest report of promotional emails in Yahoo Mail for review and approval before deletion
id: 0f63e3d4-d4ef-465d-87a8-6365cb2b0bd2
index_schema_version: 1
---

Generate a digest report of promotional emails proposed for deletion from Yahoo Mail inbox.

**Objective:** Review Yahoo Mail inbox and create a detailed report of promotional and marketing emails that could be deleted, along with recommended actions. The user will then review this digest and provide approval before any actual deletion occurs.

**Email Classification Rules:**

CANDIDATES FOR DELETION (promotional/marketing/spam):
- All newsletter subscriptions and marketing emails
- Social media notifications (Instagram, Facebook, TikTok, Twitter, etc.)
- Shopping platforms and discount offers (Amazon, Aliexpress, eBay, Shopify, etc.)
- Event promotions and entertainment offers
- Advertising and promotional content from any sender
- Repeat promotional senders identified in previous cleanup sessions

KEEP (legitimate service and personal emails):
- Utility bills: E.ON Myline, Hidroelectrica
- Banking and financial: Banca Transilvania, BLOC ADMIN, NETOPIA, PayPal (only account security alerts, not promotional)
- Security alerts: Google (account security, recovery codes)
- Service notifications: Yahoo Mail system messages, email verification codes
- Authentication codes and OTP (one-time passwords)
- Domain registrar emails
- Personal correspondence from known contacts
- Work-related emails
- Any utility or service provider communications

**Steps to Execute:**

1. Open mail.yahoo.com in the browser
2. Review unread emails at the top of the inbox (scroll through the current day's mail)
3. For each promotional email identified:
   - Note the sender name and email count
   - Take a screenshot of the email to document the classification
   - Track the sender in a list for the report
4. Continue scrolling through today's emails and identify all promotional senders
5. **Proactive review phase:** If available, also review older emails:
   - Scroll down to access emails from previous days
   - Review promotional emails in batches of approximately 100 emails
   - Document senders and counts
6. **Create a digest report** with the following information:
   - **Proposed for Deletion:** Organized by category (newsletters, shopping, social media, other)
   - **Sender List:** Complete list of promotional senders with estimated email counts
   - **Unsubscribe Candidates:** Senders where unsubscribe links may be available
   - **Current Inbox Status:** Current unread email count
   - **Confidence Level:** For each sender (high/medium/low confidence it's promotional)
   - **Any issues encountered:** e.g., emails with link overlays preventing right-click menu
   - **Date and time of review:** When this digest was created

**Expected Output:** A detailed digest report (formatted as text or document) showing:
- Summary: Total emails proposed for deletion, number of senders
- Categorized list of senders with email counts and confidence levels
- Clear formatting for easy review
- **ACTION REQUIRED:** Section at the end asking user to review and approve before deletion proceeds

**Constraints & Notes:**
- Generate a REPORT only—do not delete any emails
- Be methodical: ensure each sender is identified as promotional before adding to the report
- Include confidence levels to help the user make informed decisions
- If uncertain whether an email is promotional or legitimate, err on the side of excluding it from the deletion list
- Document the briefing in a clear, readable format for easy reference
- Save the digest report with a timestamp so the user can reference it later
