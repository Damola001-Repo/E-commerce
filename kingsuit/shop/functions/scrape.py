import json  # Import the JSON module
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://row.representclo.com/collections/mens-new-arrivals-all?page=1"

class Scraper:
    def __init__(self, url):
        self.url = url
        self.driver = None  # Do not initialize the driver here
        self.products = []

        # Set up Chrome options
        self.chrome_options = Options()
        self.chrome_options.add_argument("--disable-search-engine-choice-screen")

        # Set up the ChromeDriver service
        self.service = Service(r'C:\Users\damol\Desktop\PythonProject\kingsuit\kingsuit\shop\functions\chromedriver-win64\chromedriver.exe')

    def get_products(self):
        # Initialize the driver only when this method is called
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)

        product_data = []  # List to store all products
        num = 1  # Start from page 1

        while True:  # Infinite loop, will break when no products are found
            print(f"Scraping page {num}...")
            self.driver.get(self.url + str(num))
            products = self.driver.find_elements(By.CSS_SELECTOR, "a.flex.flex-col.w-full.group")

            # Break the loop if no products are found
            if not products:
                print(f"No products found on page {num}. Stopping.")
                break

            print(f"Number of products found on page {num}: {len(products)}")

            for product in products:
                # Extract product details
                title = product.find_element(By.CSS_SELECTOR, "h3.font-global_weight.text-xs").text
                price = product.find_element(By.CSS_SELECTOR, "span.uppercase.font-normal").text
                image_url = product.find_element(By.CSS_SELECTOR, "img.block.object-cover.h-full.w-full").get_attribute("src")

                # Append the product data to the list
                product_data.append({
                    "title": title,
                    "price": price.strip('$'),
                    "image_url": image_url
                })

            num += 1  # Go to the next page

        self.driver.quit()  # Close the driver after scraping
        return product_data


if __name__ == "__main__":
    scraper = Scraper("https://row.representclo.com/collections/mens-new-arrivals-all?page=1")
    
    products = scraper.get_products()
    print(json.dumps(products, indent=4))  # Print the product data in a readable format