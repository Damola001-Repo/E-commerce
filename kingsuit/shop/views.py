from django.shortcuts import render
from django.views import View  # Import the base View class
from .functions.scrape import get_products
from .models import Product  # Import the Product model

# Create your views here.
class ProductListView(View):  # Inherit from View
    def get(self, request):
        products = get_products()

        for product in products:
            # Assuming you have a Product model to save the scraped data
            Product.objects.create(
                name=product['title'],
                description=product.get('description', ''),
                price=product['price']
            )
        # Fetch all products from the database to display
            
        # Here you would typically fetch products from the database
        products = [
            {'name': 'Product 1', 'price': 10.00},
            {'name': 'Product 2', 'price': 20.00},
            {'name': 'Product 3', 'price': 30.00},
        ]
        return render(request, 'shop/index.html', {'products': products})