from django.db import models

# Reviews
class Review(models.Model):
    date_review = models.DateField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    stars = models.PositiveSmallIntegerField(default=5)

# Contact
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    reason = models.CharField(max_length=150)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
     
#Patient