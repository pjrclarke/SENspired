from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField('Image', null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(User, through='Attendee', related_name='attended_events')
    max_capacity = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)


    def __str__(self):
        return self.title

class Attendee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
    
class Booking(models.Model):
    
    STATUS_CHOICES = [
        ('waiting', 'Waiting Approval'),
        ('approved', 'Approved'),
        ('denied', 'Denied'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=255)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='waiting')

    def __str__(self):
        return f"{self.event_name} - {self.date}"