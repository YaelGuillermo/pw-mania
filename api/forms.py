from django import forms
from main.models import *

class CreateCountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = [
            "name",
            "abbreviation",
            "image",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "abbreviation": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control", "id": "id_image"}),
        }

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_staff']

        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'password': forms.PasswordInput(attrs={"class": "form-control"}),
            'is_staff': forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "user",
            "birth_date",
            "biography",
            "image",
        ]
        widgets = {
            "user": forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"}),
            "birth_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "biography": forms.Textarea(attrs={"class": "form-control", "cols": "5"}),
            "image": forms.FileInput(attrs={"class": "form-control", "id": "id_image"}),
        }


class CreateGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = [
            "name",
            "description",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "cols": "5"}),
        }

class CreateArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = [
            "name",
            "nickname",
            "image",
            "description",
            "birth_date",
            "nationality",
            "genres",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "nickname": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control", "id": "id_image"}),
            "description": forms.Textarea(attrs={"class": "form-control", "cols": "5"}),
            "birth_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "nationality": forms.Select(attrs={"class": "form-control"}),
            "genres": forms.SelectMultiple(attrs={"class": "form-control"}),
        }

class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            "title",
            "artists",
            "genres",
            "date",
            "image",
            "description",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "artists": forms.SelectMultiple(attrs={"class": "form-control"}),
            "genres": forms.SelectMultiple(attrs={"class": "form-control"}),
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "image": forms.FileInput(attrs={"class": "form-control", "id": "id_image"}),
            "description": forms.Textarea(attrs={"class": "form-control", "cols": "5"}),
        }

class CreateSongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = [
            "title",
            "genres",
            "duration",
            "video",
            "album",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "genres": forms.SelectMultiple(attrs={"class": "form-control"}),
            "duration": forms.TimeInput(attrs={"class": "form-control", "placeholder": "MM:SS"}),
            "video": forms.TextInput(attrs={"class": "form-control"}),
            "album": forms.Select(attrs={"class": "form-control"}),
        }

class CreatePlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = [
            "user",
            "title",
            "songs",
            "description",
        ]
        widgets = {
            "user": forms.Select(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "songs": forms.SelectMultiple(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "cols": "5"}),
        }

class CreateDiscForm(forms.ModelForm):
    class Meta:
        model = Disc
        fields = [
            "user",
            "title",
            "genres",
            "duration",
            "video",
        ]
        widgets = {
            "user": forms.Select(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "genres": forms.SelectMultiple(attrs={"class": "form-control"}),
            "duration": forms.TextInput(attrs={"class": "form-control", "placeholder": "HH:MM:SS"}),
            "video": forms.TextInput(attrs={"class": "form-control"}),
        }

class CreateLikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = [
            "user",
            "song",
        ]
        widgets = {
            "user": forms.Select(attrs={"class": "form-control"}),
            "song": forms.Select(attrs={"class": "form-control"}),
        }
