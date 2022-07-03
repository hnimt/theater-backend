from django.contrib.auth import get_user_model
from django.db import models

from core.models import ModelBase
from movie.models import Movie


class Comment(ModelBase):
    user = models.ForeignKey(get_user_model(), related_name="comments", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name="comments", on_delete=models.CASCADE)
    value = models.TextField()
    is_updated = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"User: {self.user} | Movie: {self.movie}"
