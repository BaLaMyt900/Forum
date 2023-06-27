from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, UpdateView
from announcement.forms import AnnounceForm
from announcement.models import Announcement, Category, Response
from django.http import JsonResponse


class AnnouncementCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """ Страница создания объявления """
    model = Announcement
    form_class = AnnounceForm
    template_name = 'announce/new.html'
    permission_required = 'announcement.add_announcement'

    def form_valid(self, form):
        """ Сохранение объявления с захватом автора из request """
        announce = form.save(commit=False)
        announce.author = self.request.user
        announce.save()
        form.save_m2m()
        return redirect('/')

    def get_context_data(self, **kwargs):
        """ выгрузка категорий для создания раиальных кнопок выбора """
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().values('pk', 'name')
        return context


class AnnounceView(DetailView):
    """ Страница просмотра одного объявления """
    model = Announcement
    template_name = 'announce/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['response'] = Response.objects.filter(announce=self.object, is_accept=True)
        return context


class AnnounceUpdate(UpdateView):  # TODO: Доделать редактирование
    model = Announcement
    template_name = 'announce/new.html'
