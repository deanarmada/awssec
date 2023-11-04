from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = ['comment', ]
        fields = ['blog', 'user', 'comment']
        widgets = {'blog': forms.HiddenInput(),
                   'user': forms.HiddenInput()}
