from django.forms import ModelForm, HiddenInput
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'publication_date']
        widgets = {'author': HiddenInput()}
