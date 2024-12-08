import requests
from bs4 import BeautifulSoup

url = 'https://free-proxy-list.net/'

def scraper():
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure we got a valid response
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all rows in the proxy table
        rows = soup.select("table.table-striped tbody tr")
        if not rows:
            print("No proxy data found!")
            return []

        # Extract proxy details from rows
        proxies_list = []
        for row in rows:
            proxy = row.find("td").text.strip()  # Extract first cell (IP)
            proxies_list.append(proxy)
        
        print(proxies_list)
        return proxies_list

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching proxies: {e}")
        return []

if __name__ == '__main__':
    proxies = scraper()
    if proxies:
        print("Proxies fetched successfully!")
    else:
        print("No proxies found!")
