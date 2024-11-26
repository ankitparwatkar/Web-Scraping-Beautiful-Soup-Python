import pandas as pd
import requests
from bs4 import BeautifulSoup

# Step 1: Make a request to the website
url = 'https://www.espncricinfo.com/records/most-runs-in-career-284269'  # Replace with the target URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Step 2: Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

#     # Step 3: Extract Data
#     # Example: Let's say we want to scrape all headings (h1, h2, h3)
#     headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p'])

#     for heading in headings:
#         print(heading.text.strip())  # Print the text of each heading

#     # Example: Scraping a list of items (assuming they're in <li> tags)
#     items = soup.find_all('a')
#     items = soup.find_all('td')
#     for item in items:
#         print(item.text.strip())  # Print each list item's text

# else:
#     print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

data = []
table = soup.find('table')  # Adjust as necessary
for row in table.find_all('tr'):
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)

# Step 3: Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('output.csv', index=False, header=False)  # Adjust header as needed

