from django import forms
from .models import Binta

class PostForm(forms.ModelForm):

    class Meta:
        model = Binta
        fields = ('title', 'text',)