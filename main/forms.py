from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.auth.forms import forms
from .models import Category, Announcement


class AnnounceForm(forms.ModelForm):
    """ Форма создания нового объявления """
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=True,
        to_field_name='pk',
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Announcement
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3', 'required': 'required'}),
        }
        labels = {
            'title': 'Заголовок',
            'text': 'Текс статьи',
            'category': 'Категория'
        }
