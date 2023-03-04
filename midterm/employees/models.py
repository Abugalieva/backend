from django.db import models

# Create your models here.
class Employee(models.Model):
    full_name = models.CharField(max_length=255, null=False)
    position = models.CharField(max_length=255, null=False)
    salary = models.IntegerField(default=0, null=False)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

