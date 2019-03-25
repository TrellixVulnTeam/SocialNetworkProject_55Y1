from django import forms
from .models import Tweet


class TweetModelForm(forms.ModelForm):
    tweet = forms.CharField(widget= forms.Textarea(attrs={"class":"form-control"}),label='')
    class Meta:
        model = Tweet
        exclude = ['creation', 'user', 'update']