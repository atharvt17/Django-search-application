from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    address = models.TextField()
    rating_text = models.CharField(max_length=255, null=True, blank=True)
    aggregate_rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name
