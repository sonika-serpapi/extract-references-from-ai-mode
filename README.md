# Tracking citations in Google's AI Mode using SerpApi's Google AI Mode API and Python

Code examples for blog post: Find and Track Google's AI Mode Cited Sources

You can read the blog post here: https://serpapi.com/blog/find-and-track-googles-ai-mode-cited-sources/

---

**Getting Started With Using SerpApi**

You can use our APIs in multiple languages, but for the purposes of this blog post, I've used Python.

To begin scraping data, first, create a free account on serpapi.com. You'll receive 250 free search credits each month to explore the API.

Get your SerpApi API Key from this page: https://serpapi.com/manage-api-key. 

Set your API key in an environment variable, instead of directly pasting it in the code. For this tutorial, I have saved the API key in an environment variable named "SERPAPI_API_KEY" in my .env file. [Optional but Recommended]

Next, on your local computer, you need to install a couple libraries:

`pip install -r requirements.txt`

---

**Run The Code**

Head to the project folder and run the code file using `python google_ai_mode_citations.py`

---

**Sample Output**

For a list of questions: 

```
list_of_questions = [
        "What are the best running shoes for beginners?",
        "Running shoes vs walking shoes: what are the differences?",
        "How to choose the right running shoes for flat feet?",
        "What are the top-rated running shoes for long-distance running?",
        "Are expensive running shoes worth the investment?",
        "Top 20 running shoes",
        "Best running shoes for trail running",
        "How to properly care for running shoes?",
        "What are the latest innovations in running shoe technology?",
        "How do running shoes impact overall running performance?"
    ]
```

And a website domain: `nike.com`

The resulting CSV looks like this:

<img width="1097" height="724" alt="Screenshot 2025-12-04 at 4 35 12 PM" src="https://github.com/user-attachments/assets/5d7722c4-abdf-43a9-9522-065c9eca4b9f" />

