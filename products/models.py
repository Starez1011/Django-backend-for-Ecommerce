from django.db import models
from accounts.models import User
import uuid
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    uploader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'product'
    def __str__(self):
        return self.name + self.category.name