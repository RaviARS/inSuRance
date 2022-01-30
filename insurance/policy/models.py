from django.db import models
from django.core.exceptions import ValidationError


class Policy(models.Model):
    """ Policy data model. """
    id = models.AutoField(primary_key=True)
    Policy_id = models.PositiveIntegerField()
    # Date_of_Purchase = models.DateField(null=True)
    Date_of_Purchase = models.CharField(max_length=28)
    Customer_id = models.PositiveIntegerField()
    Fuel = models.CharField(max_length=8)
    VEHICLE_SEGMENT = models.CharField(max_length=8)
    Premium = models.PositiveIntegerField()
    bodily_injury_liability = models.BooleanField(default=0)
    personal_injury_protection = models.BooleanField(default=0)
    property_damage_liability = models.BooleanField(default=0)
    collision = models.BooleanField(default=0)
    comprehensive = models.BooleanField(default=0)
    Customer_Gender = models.CharField(max_length=8)
    Customer_Income_group = models.CharField(max_length=8)
    Customer_Region = models.CharField(max_length=8)
    Customer_Marital_status = models.BooleanField(default=0)
