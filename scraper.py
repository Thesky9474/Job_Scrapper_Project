import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0"
}

titles, companies, locations, durations, stipends = [], [], [], [], []

for page in range(1, 6):  # Scrape first 5 pages
    url = f"https://internshala.com/internships/python-internship/page-{page}"
    print(f"Scraping: {url}")
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    cards = soup.find_all("div", class_="individual_internship")
    if not cards:
        print("No more internships found. Ending.")
        break

    for card in cards:
        try:
            title_tag = card.find("a", class_="job-title-href")
            title = title_tag.text.strip() if title_tag else "N/A"

            company_tag = card.find("p", class_="company-name")
            company = company_tag.text.strip() if company_tag else "N/A"
            
            detail_box = card.find("div", class_="individual_internship_details")
            detail_rows = detail_box.find_all("div", class_="row-1-item") if detail_box else []

            # Extract location
            location_tag = detail_box.find("div", class_="row-1-item locations") if detail_box else None
            location = location_tag.find("a").text.strip() if location_tag else "N/A"

            # Extract stipend
            stipend_tag = detail_box.find("span", class_="stipend") if detail_box else None
            stipend = stipend_tag.text.strip() if stipend_tag else "N/A"

            # Extract duration (3rd row-1-item)
            duration_tag = detail_rows[2].find("span") if len(detail_rows) >= 3 else None
            duration = duration_tag.text.strip() if duration_tag else "N/A"

            title = title_tag.text.strip() if title_tag else "N/A"
            company = company_tag.text.strip() if company_tag else "N/A"

            # Append data
            titles.append(title)
            companies.append(company)
            locations.append(location)
            durations.append(duration)
            stipends.append(stipend)

        except Exception as e:
            print("Error parsing a card:", e)
            continue

# Save to CSV
df = pd.DataFrame({
    "Title": titles,
    "Company": companies,
    "Location": locations,
    "Duration": durations,
    "Stipend": stipends
})

df.to_csv("internshala_jobs.csv", index=False)
print(f"\n✅ Saved {len(df)} job listings to 'internshala_jobs.csv'")
