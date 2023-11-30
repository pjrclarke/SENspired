from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class Attendee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username} - {self.event.title}"