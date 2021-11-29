from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    username = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=50, default='')
    password2 = models.CharField(max_length=50, default='')
    question1 = models.CharField(max_length=200, default='')
    question2 = models.CharField(max_length=200, default='')
    answer1 = models.CharField(max_length=200, default='')
    answer2 = models.CharField(max_length=200, default='')
    # saved_trips = models.CharField(max_length=200, default='')
    # booked_trips = models.CharField(max_length=200, default='')
    # reviews = models.CharField(max_length=200, default='')
    # time_stamp = models.DateTimeField(auto_now_add=True, editable=False)
    def __str__(self):
        return self.name

# class Reviews(models.Model):
#     first_name = models.CharField(max_length=20)
#     reviews = models.CharField(max_length=200)
#     time_stamp = models.DateTimeField('date created')
#     def __str__(self):
#         return self.reviews

class BookedTrips(models.Model):
    user_id = models.CharField(max_length=200,default='0')
    trip_name = models.CharField(max_length=200,default='')
    user_phone = models.CharField(max_length=200,default='')
    user_email = models.CharField(max_length=200,default='')
    user_message = models.TextField(blank=True)
    trip_name = models.CharField(max_length=200,default='')

class SavedTrips(models.Model):
    user_id = models.CharField(max_length=200,default='0')
    trip_name = models.CharField(max_length=200,default='')
    user_phone = models.CharField(max_length=200,default='')
    user_email = models.CharField(max_length=200,default='')
    trip_name = models.CharField(max_length=200,default='')