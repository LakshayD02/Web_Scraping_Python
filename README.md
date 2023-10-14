# Web_Scraping_Python
A program that extracts product information, such as names, prices and ratings from an online ecommerce website and stores the data in a structured format like a CSV file. 

You provide the URL of the e-commerce website you want to scrape.
A GET request is sent to the URL to retrieve the HTML content of the page.
BeautifulSoup is used to parse the HTML and extract product information. You will need to inspect the HTML structure of the website and adjust the selectors accordingly.
The extracted data is stored in a list, and then it's written to a CSV file ('product_data.csv').
