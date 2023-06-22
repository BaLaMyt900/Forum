from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView
from .forms import AnnounceForm
from .models import Announcement, Response


class IndexView(ListView):
    """ Показ стартовой страницы с выгрузкой последних постов """
    model = Announcement
    template_name = 'index.html'


class AnnounceView(DetailView):
    """ Страница просмотра отдельного объявления """
    model = Announcement


class NewAnnounceView(CreateView):
    """ Страница создания объявления """
    model = Announcement
    form_class = AnnounceForm
    template_name = 'announce/new.html'

    def form_valid(self, form):
        announce = form.save(commit=False)
        announce.author = self.request.user
        announce.save()
        form.save_m2m()
        return redirect('/')
