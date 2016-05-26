from django import forms
from emailform.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # exclude = ['author', 'updated', 'created', ]
        fields = ['text', 'last', 'email']
        widgets = {
            'text': forms.TextInput(
                attrs={'id': 'post-text', 'required': True, 'placeholder': 'First Name'}
            ),
            'last': forms.TextInput(
                attrs={'id': 'last-text', 'required': True, 'placeholder': 'Last Name'}
            ),
            'email': forms.TextInput(
                attrs={'id': 'email-text', 'required': True, 'placeholder': 'Email Address'}
            ),
        }
