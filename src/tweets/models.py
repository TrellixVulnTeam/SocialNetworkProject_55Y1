from django.db import models
from django.conf import settings
from .validators import validate_bad_content, validate_blank_content
from django.urls import reverse_lazy
# Create your models here.


class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    tweet = models.CharField(max_length=80,
                validators=[validate_bad_content,
                            validate_blank_content])
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse_lazy("tweet:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.tweet)