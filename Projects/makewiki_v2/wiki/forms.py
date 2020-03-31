from django import forms
from wiki.models import Page, Post


class PageForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta:
        model = Page
        fields = ['title', 'content']

class PostForm(forms.ModelForm):
    """ Render and process a form based on Post Model. """
    class Meta:
        model = Post
        fields = ['title', 'content']
