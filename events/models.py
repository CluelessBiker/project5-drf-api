from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    """
    Events model for database.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    price = IntegerField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Order events by date of event.
        """
        ordering = ['-date']

    def __str__(self):
        return f'{self.title} {self.date}'
