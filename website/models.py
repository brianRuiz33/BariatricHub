from django.db import models

# Reviews
class Review(models.Model):
    date_review = models.DateField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    stars = models.PositiveSmallIntegerField(default=5)

    @property
    def stars_range(self):
        return range(self.stars)

# Contact
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    reason = models.CharField(max_length=150)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    was_contacted = models.BooleanField(default=False)
    is_spam = models.BooleanField(default=False)

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
    travel = models.BooleanField(default=True)
    forms_of_contact = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    was_contacted = models.BooleanField(default=False)

    def weight_in_kg(self):
        if self.weight_unit == "lb":
            return round(self.weight * 0.453592, 2)
        return self.weight

    def weight_in_lb(self):
        if self.weight_unit == "kg":
            return round(self.weight * 2.20462, 2)
        return self.weight
    
    def weight_to_lose_in_kg(self):
        if self.weight_to_lose_unit == "lb":
            return round(self.weight_to_lose * 0.453592, 2)
        return self.weight_to_lose
    
    def weight_to_lose_in_lb(self):
        if self.weight_to_lose_unit == "kg":
            return round(self.weight_to_lose * 2.20462, 2)
        return self.weight_to_lose

      
    def bmi(self):
        height_m = self.height_cm / 100
        return round(self.weight_in_kg() / (height_m ** 2), 2)
    


def __str__(self):
        return f"{self.full_name} - {self.phone}"