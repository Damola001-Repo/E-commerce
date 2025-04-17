from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

# Set up the ChromeDriver service
service = Service('chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the website
driver.get("https://row.representclo.com/collections/mens-new-arrivals-all?page=1")


def get_products():
    # Find all product elements on the page
    products = driver.find_elements(By.CLASS_NAME, "product-card")
    product_data = []

    for product in products:
        # Extract product details
        title = product.find_element(By.CLASS_NAME, "product-card-title").text
        price = product.find_element(By.CLASS_NAME, "product-card-price").text
        image_url = product.find_element(By.TAG_NAME, "img").get_attribute("src")

        # Append the product data to the list
        product_data.append({
            "title": title,
            "price": price.strip('$'),
            "image_url": image_url
        })

    return product_data

if __name__ == "__main__":
    # Get the product data
    products = get_products()

    # Print the product data
    for product in products:
        print(f"Title: {product['title']}")
        print(f"Price: {product['price']}")
        print(f"Image URL: {product['image_url']}")
        print("-" * 40)

    # Close the browser
    driver.quit()