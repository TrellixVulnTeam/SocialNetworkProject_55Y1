from django.contrib import admin
from .models import Tweet


class TweetModelAdmin(admin.ModelAdmin):
  #  list_display = [field.name for field in Tweet._meta.get_fields()]
    class Meta:
        model = Tweet



admin.site.register(Tweet, TweetModelAdmin)