from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


# Class provided by DRF-API walkthrough.
class Comment(models.Model):
    """
    Comments Model.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        """
        Display comments in order of posting.
        Newest first.
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Display content instead of ID.
        """
        return self.content
