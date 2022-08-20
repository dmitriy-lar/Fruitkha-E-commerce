from django import forms
from .models import Newsletter


class NewsLetterForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
    }), label='')

    class Meta:
        model = Newsletter
        fields = '__all__'
