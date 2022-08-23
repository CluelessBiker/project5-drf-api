from django.db import models
from django.contrib.auth.models import User
from categories.models import Category


class Article(models.Model):
    """
    Articles model.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = models.TextField(blank=False)
    image = models.ImageField(
        upload_to='images/',
        default='../pexels-artem-podrez-7048043_jblpym',
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True
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
