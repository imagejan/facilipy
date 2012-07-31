from django.db import models
from django.contrib.auth.models import User

class Resource(models.Model):
	name = models.CharField(max_length=200)

class Booking(models.Model):
	user = models.ForeignKey(User)
	resource = models.ForeignKey(Resource)
	blackout = models.BooleanField(default=False)
	start = models.DateTimeField('start date and time')
	end = models.DateTimeField('end date and time')
