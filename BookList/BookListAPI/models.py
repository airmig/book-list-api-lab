from django.db import models

# Create your Book model here.
# Create Meta class inside the Book model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.IntegerField(default=0)
    class Meta:
        indexes = [models.Index(fields=['price'])]
    def __str__(self):
        return self.title