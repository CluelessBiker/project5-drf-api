from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    """
    Articles model.
    """
    category_choices = [
        ('entertainment', 'Entertainment'),
        ('events', 'Events'),
        ('in_depth', 'In-depth'),
        ('opinion', 'Opinion'),
        ('news', 'News'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = models.TextField(blank=False)
    image = models.ImageField(
        upload_to='images/',
        default='../pexels-artem-podrez-7048043_jblpym',
        blank=True
    )
    image_credit = models.CharField(max_length=200)
    category = models.CharField(
        max_length=55,
        choices=category_choices,
        default='news'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Order articles by date created.
        Display by most recent first.
        """
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.title}'
