##use this to scrape data from wiki
import os
import logging
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from dotenv import load_dotenv
from src.models.templeModel import Temple

# Setup logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv()

# Connect to MongoDB
client = MongoClient(os.getenv('MONGO_URI'))
db = client.temple_db

def get_wikipedia_data(temple_name):
    url = f"https://en.wikipedia.org/wiki/{temple_name.replace(' ', '_')}"
    response = requests.get(url)
    if response.status_code != 200:
        logging.error(f"Failed to retrieve data for {temple_name} from Wikipedia")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Scrape details
    location = "Unknown"
    built_date = "Unknown"
    description = "No description available"
    images = []

    try:
        # Find description
        description_tag = soup.find('p')
        if description_tag:
            description = description_tag.text.strip()

        # Find location and built date
        info_box = soup.find('table', class_='infobox')
        if info_box:
            rows = info_box.find_all('tr')
            for row in rows:
                header = row.find('th')
                if header:
                    header_text = header.text.strip()
                    if 'Location' in header_text:
                        location = row.find('td').text.strip()
                    elif 'Built' in header_text:
                        built_date = row.find('td').text.strip()

        # Find images
        image_elements = soup.find_all('img')
        for img in image_elements:
            if img['src'].startswith('//upload.wikimedia.org'):
                images.append(f"https:{img['src']}")
                if len(images) >= 3:
                    break

    except Exception as e:
        logging.error(f"Error scraping data for {temple_name}: {str(e)}")

    return {
        "name": temple_name,
        "location": location,
        "built_date": built_date,
        "description": description,
        "images": images
    }

def save_to_mongodb(data):
    existing_temple = db.temples.find_one({"name": data["name"]})
    if existing_temple:
        logging.info(f"Temple '{data['name']}' already exists in the database.")
    else:
        temple = Temple(
            name=data["name"],
            location=data["location"],
            built_date=data["built_date"],
            description=data["description"],
            images=data["images"]
        )
        temple.save()
        logging.info(f"Data saved for temple: {data['name']}")

def main():
    temple_name = input("Enter the name of the temple: ")
    data = get_wikipedia_data(temple_name)
    if data:
        save_to_mongodb(data)

if __name__ == "__main__":
    main()
