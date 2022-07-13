from django.db import models
from django.urls import reverse


BOTTLESIZES = (
    ('30', '1 FL. OZ. or 30 mL'), 
    ('50', '1.7 FL. OZ or 50 mL'), 
    ('75', '2.5 FL. OZ. or 75 mL'),
    ('100', '3.4 FL. OZ. or 100 mL'), 
    ('125', '4.2 FL. OZ or 125 mL'), 
)

# Create your models here.
class Fragrance(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    release_year = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'fragrance_id': self.id})


class Purchase(models.Model): 
    date = models.DateField('purchase date')
    size = models.CharField(
        max_length=3, 
        choices=BOTTLESIZES, 
        default=BOTTLESIZES[0][0]
    )
    price = models.DecimalField(max_digits=7, decimal_places=2)

    fragrance = models.ForeignKey(Fragrance, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_size_display()} on {self.date}"
