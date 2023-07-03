from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, UpdateView
from announcement.forms import AnnounceForm
from announcement.models import Announcement, Category, Response


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
        """ выгрузка категорий для создания радиальных кнопок выбора """
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
        if self.request.user == self.object.author and \
                Response.objects.filter(is_accept=False, announce=self.object).exists():
            """ Добавление на страницу неактивных откликов, если зашел автор объявления """
            context['inactive_response'] = Response.objects.filter(is_accept=False, announce=self.object)
        return context


class AnnounceUpdate(UpdateView):
    """ Страница редактирования статьи. Разрешено заходить только автору """
    model = Announcement
    template_name = 'announce/edit.html'
    form_class = AnnounceForm

    def get(self, request, *args, **kwargs):
        """ Отлов разрешения на редактирование статьи. Зайти может только автор, остальные 403 """
        if request.user != self.get_object().author:
            raise PermissionDenied
        else:
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return f'/announce/{self.object.pk}'

    def get_context_data(self, **kwargs):
        """ выгрузка категорий для создания радиальных кнопок выбора """
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().values('pk', 'name')
        return context
