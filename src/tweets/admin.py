from django.contrib import admin
from .models import Tweet
from .forms import  TweetModelForm

# Register your models here.


class TweetAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tweet._meta.get_fields()]
    # form = TweetModelForm

    class Meta:
        model = Tweet
admin.site.register(Tweet,TweetAdmin)
