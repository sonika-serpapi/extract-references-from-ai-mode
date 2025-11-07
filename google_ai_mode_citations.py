from serpapi import GoogleSearch
from dotenv import load_dotenv
import os, csv
load_dotenv() 

def get_references_from_ai_mode(question):
    params = {
        "api_key": os.environ["SERPAPI_API_KEY"],
        "engine": "google_ai_mode",
        "q": question,
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results.get("references", "")

# --- Main Execution ---
if __name__ == "__main__":
    header = ['Question', 'Domain', 'Position found', 'Links'] # Specify a list of the fields you are interested in
    with open("google_ai_mode_citations.csv", "w", encoding="UTF8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)

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
    ] # Replace with your actual list of questions
    your_website_domain = "nike.com"  # Replace with your actual domain

    for question in list_of_questions:
        references = get_references_from_ai_mode(question)
        if not references:
            position = "Not Found"
            links = "No references found"
        else:
            position = "Not Found"
            links = []
            for ref in references:
                links.append(ref.get('link', ''))
                if your_website_domain in ref.get('link', ''):
                    position = references.index(ref)
                    break
        # Write to CSV
        with open("google_ai_mode_citations.csv", "a", encoding="UTF8", newline="") as f:
            writer = csv.writer(f)
            links = '\n'.join(links) # Join links with newline for better readability in CSV
            writer.writerow([question, your_website_domain, position, links])