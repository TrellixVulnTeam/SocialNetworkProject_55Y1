from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import  Q
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Tweet
from .forms import TweetModelForm
from .mixin import FormUserMixin, AllowedUserMixin


class DetailViewT(DetailView):
    template_name = 'detail_view.html'
    queryset = Tweet.objects.all()


class ListViewT(ListView):
    template_name = 'list_view.html'

    def get_queryset(self):
        query = self.request.GET.get("q", None)
        return Tweet.objects.all() if not query else Tweet.objects.all().filter(
            Q(tweet__icontains=query) |
            Q(user__username__icontains=query)|
            Q(user__username__startswith=query) |
            Q(created__icontains=query)|
            Q(tweet__startswith=query)

        )
    def get_context_data(self, *args, **kwargs ):
        context = super(ListViewT, self).get_context_data(*args,**kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy('tweet:create')

        return context

class CreateViewT(FormUserMixin, CreateView, LoginRequiredMixin):
        form_class = TweetModelForm
        template_name = 'create_view.html'


class UpdateViewT(AllowedUserMixin, UpdateView, LoginRequiredMixin):
        queryset = Tweet.objects.all()
        template_name = 'update_view.html'
        form_class = TweetModelForm
        # success_url = "/tweet/"

class DeleteViewT (LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = 'delete_view.html'
    success_url = reverse_lazy("tweet:list")
    login_url = '/admin/'

