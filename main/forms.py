from django.contrib.auth.forms import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Announcement, Category


class AnnounceForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ('title', 'category', 'text')
        widgets = {
            'text': SummernoteWidget()
        }
