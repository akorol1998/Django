from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.title}: {self.content}'



# class User(models.Model):
#     name = models.CharField(max_length=50)
#     surname = models.CharField(max_length=50)
#     b_date = models.DateField()
#     description = models.TextField(max_length=300)
#     fav_film = models.CharField(max_length=50)

#     def __str__(self):
#         return f"{self.name}, {self.surname}, {self.b_date}, {self.description}, {self.fav_film}"

# class Company(models.Model):
#     name = models.CharField(max_length=50)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.name} -> {self.user}"
