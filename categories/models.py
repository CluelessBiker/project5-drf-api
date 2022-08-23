from django.db import models


class Category(models.Model):
    """
    Model to supply categories to Articles app.
    """
    category_choices = [
        ('entertainment', 'Entertainment'),
        ('events', 'Events'),
        ('in_depth', 'In Depth'),
        ('opinion', 'Opinion'),
        ('news', 'News'),
    ]

    created_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=55,
        choices=category_choices,
        default='none'
    )

    class Meta:
        """
        Order categories.
        """
        ordering = ['category']

    def __str__(self):
        """
        Return Category name.
        """
        return f'Category: {self.category}'
