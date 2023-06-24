from django.db import models

# Create your models here.
ITEM_SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('P', 'Portion'),
)


class Menu(models.Model):
    name = models.CharField(max_length=30)


class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, help_text="Ensure you provide some description of the ingredients")
    size = models.CharField(choices=ITEM_SIZES, max_length=1)
    calories = models.IntegerField(help_text="Calorie count should reflect <b>size</b> of the item")


class Store(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)

    def save(self, *args, **kwargs):
        super(Store, self).save(*args, **kwargs)
