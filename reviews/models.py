from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def average_rating(self):
        reviews = self.reviews.all()
        return sum(r.rating for r in reviews) / len(reviews) if reviews else 0

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    feedback = models.TextField()

    class Meta:
        unique_together = ['user', 'product']
