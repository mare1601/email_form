from django import forms
from emailform.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # exclude = ['author', 'updated', 'created', ]
        fields = ['text']
        widgets = {
            'text': forms.TextInput(
                attrs={'id': 'post-text', 'required': True, 'placeholder': 'Say something...'}
            ),
            #'last': forms.TextInput(
            #    attrs={'id': 'post-text', 'required': True, 'placeholder': 'First Name'}
            #),
            #'email': forms.TextInput(
            #    attrs={'id': 'post-text', 'required': True, 'placeholder': 'First Name'}
            #),
        }
