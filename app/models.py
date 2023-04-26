from django.db import models
from django.core import validators
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField(validators=[validators.MinValueValidator(18)])
    mobile=models.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    email=models.EmailField(validators=[validators.RegexValidator('[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}')])
    def __str__(self):
        return self.name