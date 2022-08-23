from django.db import models
from django.contrib.auth.models import User


# Class provided by DRF-API walkthrough.
# Modifications have been made.
class Post(models.Model):
    """
    Posts Model related to Owner/User.
    """
    music_medium_choices = [
        ('none', 'None'),
        ('cassette', 'Cassette'),
        ('CD', 'CD'),
        ('minidisc', 'Minidisc'),
        ('mp3', 'mp3'),
        ('radio', 'Radio'),
        ('vinyl', 'Vinyl'),
    ]

    beverage_choices = [
        ('none', 'None'),
        ('water', 'Water'),
        ('juice', 'Juice'),
        ('soda', 'Soda'),
        ('tea', 'Tea'),
        ('coffee', 'Coffee'),
        ('wine', 'Wine'),
        ('beer', 'Beer'),
        ('cocktail', 'Cocktail'),
        ('spirits', 'Spirits'),
    ]

    artistic_medium_choices = [
        ('none', 'None'),
        ('acrylic_paint', 'Acrylic paint'),
        ('clay', 'Clay'),
        ('coding', 'Coding'),
        ('coloured_pencils', 'Coloured pencils'),
        ('digital', 'Digital'),
        ('glass', 'Glass'),
        ('markers', 'Markers'),
        ('metal', 'Metal'),
        ('oil_paint', 'Oil paint'),
        ('photography', 'Photography'),
        ('spray_paint', 'Spray paint'),
        ('videography', 'Videography'),
        ('water_colours', 'Water colours'),
        ('wood', 'Wood'),
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
        max_length=20,
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
