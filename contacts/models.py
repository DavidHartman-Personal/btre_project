from django.db import models
from datetime import datetime

class Contact(models.Model):
    listing = models.CharField(max_length=200)
    # We only need the listing_id so no need to import the whole Listing model
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    # We are not going to require the user to be a registered and logged in user so make this optional
    user_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.name


