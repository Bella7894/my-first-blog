from django import forms
from .models import post 

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)