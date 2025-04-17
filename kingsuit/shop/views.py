from django.shortcuts import render
from django.views import View
from .functions.scrape import Scraper
from .models import Product

class ProductListView(View):
    def get(self, request):
        # Call the scraping function to get product data
        # scraper = Scraper("https://row.representclo.com/collections/mens-new-arrivals-all?page=")
        # scraped_products = scraper.get_products()

        # # Save the scraped data to the database
        # for product in scraped_products:
        #     Product.objects.update_or_create(
        #         name=product['title'],  # Match by name
        #         defaults={
        #             'name': product['title'],
        #             'price': product['price'],
        #             'image': product['image_url']
        #         }
        #     )

        # Fetch all products from the database to display
        products = Product.objects.all()
        return render(request, 'shop/index.html', {'products': products})