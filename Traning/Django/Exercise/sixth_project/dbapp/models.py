from django.db import models


class Student(models.Model):
    sname = models.CharField(max_length=30)
    sbranch = models.CharField(max_length=20)
    sper = models.FloatField()
    def __str__(self):
        return self.sname

    
# Create your models here.
