from django.db import models

# Create your models here.
class Calculation(models.Model):
    first_value = models.FloatField()  # For decimal or floating-point numbers
    second_value = models.FloatField()  # For decimal or floating-point numbers
    result = models.FloatField()  # For storing the calculated result

    # Optional: Add a string representation for better admin readability
    def __str__(self):
        return f"{self.first_value} + {self.second_value} = {self.result}"
