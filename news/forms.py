from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from news.models import Comment


class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2")

    def save(self, commit=False):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        if commit:
            user.save()
            
        return user
    

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("comment",)