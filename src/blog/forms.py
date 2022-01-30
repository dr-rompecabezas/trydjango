from typing import ContextManager
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # Optional override default
    # title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Title"}))
    # author      = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Author"}))
    # content     = forms.CharField(label='', widget=forms.Textarea(
    #     attrs={
    #         "placeholder": "Content",
    #         "class": "article",
    #         "rows": 10,
    #         "cols": 30
    #         }
    #     )
    # )
    # category    = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={"placeholder": "Category"}))

    class Meta:
        model = Article
        fields = [
            'title',
            'author',
            'content',
            'category',
            'active'
        ]
