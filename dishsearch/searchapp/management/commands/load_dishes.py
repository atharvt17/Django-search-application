import csv
import json
from django.core.management.base import BaseCommand
from searchapp.models import Restaurant, Dish

class Command(BaseCommand):
    help = 'Load dishes and restaurants from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                restaurant_name = row['name']
                restaurant_location = row['location']
                
                # Try to parse full_details and handle missing or invalid JSON

                try:
                    full_details = json.loads(row['full_details']) if row['full_details'] else {}
                    restaurant_address = full_details.get('location', {}).get('address', '')
                    aggregate_rating = full_details.get("user_rating", {}).get("aggregate_rating", None)
                    rating_text = full_details.get("user_rating", {}).get("rating_text", "")
                    
                    
                    if aggregate_rating:
                        aggregate_rating = float(aggregate_rating)
                except (json.JSONDecodeError, KeyError, ValueError):
                    restaurant_address = ''
                    aggregate_rating = None
                    rating_text = ''

                items = row['items']
                try:
                    items = json.loads(items) if items else {}
                except json.JSONDecodeError:
                    items = {}

                restaurant, created = Restaurant.objects.get_or_create(
                    name=restaurant_name,
                    location=restaurant_location,
                    defaults={'address': restaurant_address, 'rating_text': rating_text, 'aggregate_rating': aggregate_rating}
                )

                for dish_name, dish_price in items.items():

                    try:
                        price = float(dish_price.strip().split()[0])
                    except (ValueError, AttributeError):

                        # Set price to None if it can't be converted to float or is missing
                        price = None 

                    Dish.objects.create(
                        name=dish_name,
                        restaurant=restaurant,
                        price=price
                    )

        self.stdout.write(self.style.SUCCESS('Successfully loaded dishes and restaurants from CSV'))
