from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


# Class provided by DRF-API walkthrough.
class Like(models.Model):
    """
    Likes Model.
    Model related to "Owner" & Posts model.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        related_name='likes',
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Post cannot be liked more than once
        by same user.
        """
        ordering = ['-created_on']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'
