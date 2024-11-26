import pandas as pd
import requests
from bs4 import BeautifulSoup

# Step 1: Make a request to the website
url = 'https://www.worldometers.info/gdp/gdp-by-country/'  # Replace with the target URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Step 2: Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')


data = []
table = soup.find('table')  # Adjust as necessary
for row in table.find_all('tr'):
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)

# Step 3: Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('gdp.csv', index=False, header=False)  # Adjust header as needed

