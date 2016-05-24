from django import forms
from emailform.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # exclude = ['author', 'updated', 'created', ]
        fields = ['first']
        widgets = {
            'first': forms.TextInput(
                attrs={'id': 'post-text', 'required': True, 'placeholder': 'First Name'}
            ),
        }
