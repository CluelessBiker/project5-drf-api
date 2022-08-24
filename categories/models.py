from django.db import models


class Category(models.Model):
    """
    Model to supply categories to Articles app.
    """
    category_choices = [
        ('entertainment', 'Entertainment'),
        ('events', 'Events'),
        ('in_depth', 'In-depth'),
        ('opinion', 'Opinion'),
        ('news', 'News'),
    ]

    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(
        max_length=55,
        choices=category_choices,
        default='news'
    )


    class Meta:
        """
        Order categories.
        """
        ordering = ['name']

    def __str__(self):
        """
        Return Category name.
        """
        return self.name
