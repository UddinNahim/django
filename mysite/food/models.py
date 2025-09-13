from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Frestaurant%2F&psig=AOvVaw3ZxMvdY--awAGUwglDd4ev&ust=1757693191192000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCNiU-sOL0Y8DFQAAAAAdAAAAABAK")

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
    

