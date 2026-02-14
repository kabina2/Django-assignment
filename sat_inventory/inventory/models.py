from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Component(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cost = models.FloatField()
    supplier = models.CharField(max_length=100)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
