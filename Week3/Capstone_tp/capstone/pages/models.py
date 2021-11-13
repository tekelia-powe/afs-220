from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    question1 = models.CharField(max_length=200)
    question2 = models.CharField(max_length=200)
    question3 = models.CharField(max_length=200)
    saved_trips = models.CharField(max_length=200)
    booked_trips = models.CharField(max_length=200)
    reviews = models.CharField(max_length=200)
    time_stamp = models.DateTimeField('date created')
    def __str__(self):
        return self.name

# class Reviews(models.Model):
#     first_name = models.CharField(max_length=20)
#     reviews = models.CharField(max_length=200)
#     time_stamp = models.DateTimeField('date created')
#     def __str__(self):
#         return self.reviews