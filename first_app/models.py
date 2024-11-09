from django.db import models
from django.core import validators

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class PracModel(models.Model):
    auto_filled = models.AutoField(primary_key=True)
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    char_field = models.CharField(max_length=255)
    # comma_separeted_field = models.CharField(validators=[comma_separeted_field], max_length=255)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
