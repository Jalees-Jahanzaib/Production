from .models import Files ,Comment
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ( 'text',)