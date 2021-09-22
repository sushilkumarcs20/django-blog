from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    
    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class':'post-title'}),
            'text': forms.Textarea(attrs={'class':'post-text'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class':'comment-title'}),
            'text': forms.Textarea(attrs={'class':'comment-text'})
        }

