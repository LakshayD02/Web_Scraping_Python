import requests
from bs4 import BeautifulSoup
import csv

# Replace with the URL of the e-commerce website you want to scrape
url = 'https://example.com/products'

# Send a GET request to the URL
response = requests.get("https://www.amazon.in")

if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract product information (modify these selectors based on the website's structure)
    product_list = soup.find_all('div', class_='product-item')
    
    data = []

    for product in product_list:
        name = product.find('h2', class_='product-name').text.strip()
        price = product.find('span', class_='product-price').text.strip()
        rating = product.find('div', class_='product-rating').text.strip()

        data.append([name, price, rating])

    # Write the data to a CSV file
    with open('product_data.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Name', 'Price', 'Rating'])
        csvwriter.writerows(data)

    print(f"Data has been extracted and saved to 'product_data.csv'.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")


# Working of the above program

#You provide the URL of the e-commerce website you want to scrape.
#A GET request is sent to the URL to retrieve the HTML content of the page.
#BeautifulSoup is used to parse the HTML and extract product information. You will need to inspect the HTML structure of the website and adjust the selectors accordingly.
#The extracted data is stored in a list, and then it's written to a CSV file ('product_data.csv').