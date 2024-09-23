from django.db import models


class BookStore(models.Model):
    book_name=models.CharField(max_length=30)
    price=models.FloatField(default=0)
    
    def __str__(self):
        return self.book_name
    
# Create your models here.
