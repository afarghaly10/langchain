# LinkedIn Data Processing

The goal of this mini project is to develop a lightweight AI-powered application that:

1. Accepts a person's name as input.
2. Searches for the corresponding LinkedIn profile .
3. Scrapes the public profile data from LinkedIn.
4. Returns the extracted data in JSON format .
5. Uses an LLM (Large Language Model) to summarize the profile.

## High-Level Architecture

```
[User Input: Name]
        ↓
[Search for LinkedIn Profile URL]
        ↓
[Scrape Public Profile Data from LinkedIn]
        ↓
[Format Data as JSON]
        ↓
[LLM Summarizer → Generate Summary]
        ↓
[Return JSON + Summary to User]
```
