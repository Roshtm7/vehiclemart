from django.db import models

class Vehicle(models.Model):
    name=models.CharField(max_length=200)
    varient=models.CharField(max_length=200)
    description=models.TextField()
    fuel_options=(
        ("petrol","petrol"),
        ("diesel","diesel"),
        ("EV","EV"),
        ("CNG","CNG")
    )
    fuel_type=models.CharField(max_length=200,choices=fuel_options,default="petrol")
    running_km=models.PositiveIntegerField()
    color=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    brand=models.CharField(max_length=200)
    owner_option=(
        ("single","single"),
        ("seconds","seconds"),
        ("other","other")
    )
    owner_type=models.CharField(max_length=200,choices=owner_option,default="single")
    def __str__(self):
        return self.name
        
