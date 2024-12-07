import requests
from bs4 import BeautifulSoup
import re

# Function to clean and format text
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces and newlines
    text = re.sub(r'\[.*?\]', '', text)  # Remove content in brackets (optional)
    text = re.sub(r'[^\w\s.,!?\-]', '', text)  # Remove unwanted characters
    text = text.strip()
    return text

# Function to scrape and clean content from a single URL
def scrape_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract all paragraph text
        paragraphs = soup.find_all('p')
        cleaned_paragraphs = [clean_text(p.get_text()) for p in paragraphs if p.get_text()]

        return ' '.join(cleaned_paragraphs)
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ''

# Function to scrape multiple URLs and save the content to a file
def scrape_multiple_urls(urls, output_file):
    all_text = []
    for url in urls:
        print(f"Scraping {url}...")
        content = scrape_url(url)
        if content:
            all_text.append(content)

    # Combine all content and save to file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('\n\n'.join(all_text))

    print(f"Data saved to {output_file}")

# List of URLs to scrape
urls = [
    "https://en.wikipedia.org/wiki/History_of_agriculture",
    "https://en.wikipedia.org/wiki/Agriculture",
    "https://en.wikipedia.org/wiki/Glossary_of_agriculture",
    "https://www.farmfoodcareon.org/resources/did-you-know-resources/farm-glossary/",
    "https://blog.rootsofprogress.org/some-agricultural-terminology",
    "https://blog.rootsofprogress.org/six-stages-of-agriculture",
    "https://blog.rootsofprogress.org/advanced-stages-of-agriculture",
    "https://www.farmfoodcareon.org/farming-and-the-environment/lake-erie-phosphorous/",
    "https://www.farmfoodcareon.org/timing-matters/",
    "https://www.farmfoodcareon.org/farming-and-the-environment/soil-health/",
    "https://www.farmfoodcareon.org/farming-and-the-environment/soil-3-2/",
    "https://onfruit.ca/2016/06/30/how-long-do-i-run-my-drip-lines/",
    "https://www.ontario.ca/page/monitoring-soil-moisture-improve-irrigation-decisions",
    "https://www.ontario.ca/page/irrigation-scheduling-tomatoes",
    "https://www.ontario.ca/page/irrigation-scheduling-fruit-crops#:~:text=Deciding%20when%20to%20irrigate%20the,depletion%20level%20(step%202).",
    "https://www.ontario.ca/page/managing-heat-stress-fed-beef-cattle",
    "https://www.ontario.ca/page/water-requirements-livestock"
]

# Output file path
output_file = "scraped_data.txt"

# Start scraping
scrape_multiple_urls(urls, output_file)
