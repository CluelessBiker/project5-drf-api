from django.db import models
from django.contrib.auth.models import User


# Class provided by DRF-API walkthrough.
# Modifications have been made.
class Post(models.Model):
    """
    Posts Model related to Owner/User.
    """
    image_filter_choices = [
        ('_1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
    ]

    music_medium_choices = [
        'cassette',
        'CD',
        'minidisc',
        'vinyl',
        'mp3',
        'radio',
        'none',
    ]

    beverage_choices = [
        'water',
        'soda',
        'juice',
        'coffee',
        'wine',
        'beer',
        'cocktail',
        'spirits',
        'none',
    ]

    artistic_medium_choices = [
        'acrylic paint',
        'oil paint',
        'water colours',
        'spray paint',
        'coloured pencils',
        'markers',
        'photography',
        'videography',
        'digital',
        'coding',
        'wood',
        'clay',
        'metal',
        'glass',
        'none',
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../pexels-artem-podrez-7048043_jblpym',
        blank=True
    )
    image_filter = models.CharField(
        max_length=32,
        choices=image_filter_choices,
        default='normal'
    )
    music_medium = models.CharField(
        max_length=10,
        choices=music_medium_choices,
        default='none'
    )
    song_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    beverage = models.CharField(
        max_length=10,
        choices=beverage_choices,
        default='none'
    )
    artistic_medium = models.CharField(
        max_length=10,
        choices=artistic_medium_choices,
        default='none'
    )

    class Meta:
        """
        Order posts by date created.
        Display by most recent first.
        """
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title}'
