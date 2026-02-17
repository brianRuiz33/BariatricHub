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

class Appointment(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=20)
    weight = models.PositiveIntegerField()
    weight_unit = models.CharField(max_length=3, default="kg")
    height = models.PositiveIntegerField()
    height_unit = models.CharField(max_length=3, default="cm")
    procedure_of_interest = models.CharField(max_length=150)
    weight_to_lose = models.PositiveIntegerField(blank=True, null=True)
    weight_to_lose_unit = models.CharField(max_length=3, default="kg")
    prev_surgeries = models.TextField(blank=True)
    medical_conditions = models.TextField(blank=True)
    medications = models.TextField(blank=True)
    travel = models.BooleanField(default=True)
    forms_of_contact = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f"{self.full_name} - {self.phone}"