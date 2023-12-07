from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.admin.widgets import FilteredSelectMultiple

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birth_date', 'biography', 'image']
        widgets = {
            'birth_date': forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            'biography': forms.Textarea(attrs={"class": "form-control", "cols": "5", "type": "text"}),
            'image': forms.FileInput(attrs={"type": "file", "class": "form-control"}),
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        # Deshabilitar el campo de 'username' para que sea de solo lectura
        self.fields['username'].widget.attrs['readonly'] = True

class PlaylistCreateForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = [
            "title",
            "songs",
            "description",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "songs": forms.SelectMultiple(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "cols": "5"}),
        }

class DiscCreateForm(forms.ModelForm):
    class Meta:
        model = Disc
        fields = [
            "title",
            "genres",
            "duration",
            "video",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "genres": forms.SelectMultiple(attrs={"class": "form-control"}),
            "duration": forms.TextInput(attrs={"class": "form-control", "placeholder": "HH:MM:SS"}),
            "video": forms.TextInput(attrs={"class": "form-control"}),
        }
