from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 80}))

    class Meta:
        model = Post
        fields = ('title', 'description', 'image')

