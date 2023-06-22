from django.contrib.auth.forms import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Announcement, Category


class AnnounceForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=True,
        to_field_name='pk',
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = Announcement
        fields = ('title', 'category', 'text')
        widgets = {
            'text': SummernoteWidget(attrs={'class': 'bg-body'})
        }
