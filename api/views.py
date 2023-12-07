from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.hashers import make_password
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.contrib import messages
from main.models import *
from api.forms import *
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

### MENU

class DeveloperMenuView(View):
    template_name = 'api/developer_menu.html'

    def get(self, request, *args, **kwargs):
        last_artists = Artist.objects.order_by('-id')[:5]

        context = {
            'last_artists': last_artists,
        }

        return render(request, self.template_name, context)

### USER

class UserList(ListView):
    model = User
    template_name = "api/user/user_list.html"

    def get_queryset(self):
        queryset = User.objects.all()
        search_query = self.request.GET.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(id__icontains=search_query)
            )
        return queryset

class UserDetail(DetailView):
    model = User
    template_name = "api/user/user_detail.html"

class CreateUser(SuccessMessageMixin, CreateView):
    model = User
    form_class = CreateUserForm
    template_name = 'api/user/create_user.html'
    success_url = reverse_lazy('api:user_list')
    success_message = "User and Profile successfully created!"
    
    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        return response

class UpdateUser(SuccessMessageMixin, UpdateView):
    model = User
    form_class = CreateUserForm
    template_name = "api/user/update_user.html"
    success_url = reverse_lazy("api:user_list")
    success_message = "User successfully updated!"

class DeleteUser(DeleteView):
    model = User
    template_name = "api/user/delete_user.html"
    success_url = reverse_lazy("api:user_list")

### COUNTRY

class CountryList(ListView):
    model = Country
    template_name = "api/country/country_list.html"

    def get_queryset(self):
        queryset = Country.objects.all()
        search_query = self.request.GET.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(id__icontains=search_query) |
                Q(name__icontains=search_query) |
                Q(abbreviation__icontains=search_query)
            )
        return queryset

class CountryDetail(DetailView):
    model = Country
    template_name = "api/country/country_detail.html"

class CreateCountry(SuccessMessageMixin, CreateView):
    model = Country
    form_class = CreateCountryForm
    template_name = "api/country/create_country.html"
    success_url = reverse_lazy("api:country_list")
    success_message = "Country successfully created!"

class UpdateCountry(SuccessMessageMixin, UpdateView):
    model = Country
    form_class = CreateCountryForm
    template_name = "api/country/update_country.html"
    success_url = reverse_lazy("api:country_list")
    success_message = "Country successfully updated!"

class DeleteCountry(DeleteView):
    model = Country
    template_name = "api/country/delete_country.html"
    success_url = reverse_lazy("api:country_list")


### PROFILE

class ProfileList(ListView):
    model = Profile
    template_name = "api/profile/profile_list.html"

    def get_queryset(self):
        queryset = Profile.objects.all()
        search_query = self.request.GET.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(id__icontains=search_query) |
                Q(user__username__icontains=search_query) |
                Q(biography__icontains=search_query)
            )
        return queryset

class ProfileDetail(DetailView):
    model = Profile
    template_name = "api/profile/profile_detail.html"

class UpdateProfile(SuccessMessageMixin, UpdateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = "api/profile/update_profile.html"
    success_url = reverse_lazy("api:profile_list")
    success_message = "Profile successfully updated!"

class DeleteProfile(DeleteView):
    model = Profile
    template_name = "api/profile/delete_profile.html"
    success_url = reverse_lazy("api:profile_list")

### GENRE

class GenreList(ListView):
    model = Genre
    template_name = "api/genre/genre_list.html"

    def get_queryset(self):
        queryset = Genre.objects.all()
        search_query = self.request.GET.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(id__icontains=search_query) |
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        return queryset

class GenreDetail(DetailView):
    model = Genre
    template_name = "api/genre/genre_detail.html"

class CreateGenre(SuccessMessageMixin, CreateView):
    model = Genre
    form_class = CreateGenreForm
    template_name = "api/genre/create_genre.html"
    success_url = reverse_lazy("api:genre_list")
    success_message = "Genre successfully created!"

class UpdateGenre(SuccessMessageMixin, UpdateView):
    model = Genre
    form_class = CreateGenreForm
    template_name = "api/genre/update_genre.html"
    success_url = reverse_lazy("api:genre_list")
    success_message = "Genre successfully updated!"

class DeleteGenre(DeleteView):
    model = Genre
    template_name = "api/genre/delete_genre.html"
    success_url = reverse_lazy("api:genre_list")


### ARTIST

class ArtistList(ListView):
    model = Artist
    template_name = "api/artist/artist_list.html"

    def get_queryset(self):
        queryset = Artist.objects.all()
        search_query = self.request.GET.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(id__icontains=search_query) |
                Q(name__icontains=search_query) |
                Q(nickname__icontains=search_query)
            )
        return queryset

class ArtistDetail(DetailView):
    model = Artist
    template_name = "api/artist/artist_detail.html"

class CreateArtist(SuccessMessageMixin, CreateView):
    model = Artist
    form_class = CreateArtistForm
    template_name = "api/artist/create_artist.html"
    success_url = reverse_lazy("api:artist_list")
    success_message = "Artist successfully created!"
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

class UpdateArtist(SuccessMessageMixin, UpdateView):
    model = Artist
    form_class = CreateArtistForm
    template_name = "api/artist/update_artist.html"
    success_url = reverse_lazy("api:artist_list")
    success_message = "Artist successfully updated!"

class DeleteArtist(DeleteView):
    model = Artist
    template_name = "api/artist/delete_artist.html"
    success_url = reverse_lazy("api:artist_list")

### ALBUM

class AlbumList(ListView):
    model = Album
    template_name = "api/album/album_list.html"

    def get_queryset(self):
        queryset = Album.objects.all()
        search_query = self.request.GET.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(id__icontains=search_query) |
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        return queryset

class AlbumDetail(DetailView):
    model = Album
    template_name = "api/album/album_detail.html"

class CreateAlbum(SuccessMessageMixin, CreateView):
    model = Album
    form_class = CreateAlbumForm
    template_name = "api/album/create_album.html"
    success_url = reverse_lazy("api:album_list")
    success_message = "Album successfully created!"

class UpdateAlbum(SuccessMessageMixin, UpdateView):
    model = Album
    form_class = CreateAlbumForm
    template_name = "api/album/update_album.html"
    success_url = reverse_lazy("api:album_list")
    success_message = "Album successfully updated!"

class DeleteAlbum(DeleteView):
    model = Album
    template_name = "api/album/delete_album.html"
    success_url = reverse_lazy("api:album_list")

# SONG

class SongList(ListView):
    model = Song
    template_name = "api/song/song_list.html"

    def get_queryset(self):
        queryset = Song.objects.all()
        
        search_query = self.request.GET.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(id__icontains=search_query) |
                Q(title__icontains=search_query) |
                Q(duration__icontains=search_query)
            )
        return queryset

class SongDetail(DetailView):
    model = Song
    template_name = "api/song/song_detail.html"

class CreateSong(SuccessMessageMixin, CreateView):
    model = Song
    form_class = CreateSongForm
    template_name = "api/song/create_song.html"
    success_url = reverse_lazy("api:song_list")
    success_message = "Song successfully created!"

class UpdateSong(SuccessMessageMixin, UpdateView):
    model = Song
    form_class = CreateSongForm
    template_name = "api/song/update_song.html"
    success_url = reverse_lazy("api:song_list")
    success_message = "Song successfully updated!"

class DeleteSong(DeleteView):
    model = Song
    template_name = "api/song/delete_song.html"
    success_url = reverse_lazy("api:song_list")

# PLAYLIST

class PlaylistList(ListView):
    model = Playlist
    template_name = "api/playlist/playlist_list.html"

    def get_queryset(self):
        queryset = Playlist.objects.all()
        search_query = self.request.GET.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(id__icontains=search_query) |
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        return queryset

class PlaylistDetail(DetailView):
    model = Playlist
    template_name = "api/playlist/playlist_detail.html"

class CreatePlaylist(SuccessMessageMixin, CreateView):
    model = Playlist
    form_class = CreatePlaylistForm
    template_name = "api/playlist/create_playlist.html"
    success_url = reverse_lazy("api:playlist_list")
    success_message = "Playlist successfully created!"

class UpdatePlaylist(SuccessMessageMixin, UpdateView):
    model = Playlist
    form_class = CreatePlaylistForm
    template_name = "api/playlist/update_playlist.html"
    success_url = reverse_lazy("api:playlist_list")
    success_message = "Playlist successfully updated!"

class DeletePlaylist(DeleteView):
    model = Playlist
    template_name = "api/playlist/delete_playlist.html"
    success_url = reverse_lazy("api:playlist_list")

### DISC

# Vistas para Disc
class DiscList(ListView):
    model = Disc
    template_name = "api/disc/disc_list.html"

    def get_queryset(self):
        queryset = Disc.objects.all()
        search_query = self.request.GET.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(id__icontains=search_query) |
                Q(title__icontains=search_query) |
                Q(duration__icontains=search_query)
            )
        return queryset

class DiscDetail(DetailView):
    model = Disc
    template_name = "api/disc/disc_detail.html"

class CreateDisc(SuccessMessageMixin, CreateView):
    model = Disc
    form_class = CreateDiscForm
    template_name = "api/disc/create_disc.html"
    success_url = reverse_lazy("api:disc_list")
    success_message = "Disc successfully created!"

class UpdateDisc(SuccessMessageMixin, UpdateView):
    model = Disc
    form_class = CreateDiscForm
    template_name = "api/disc/update_disc.html"
    success_url = reverse_lazy("api:disc_list")
    success_message = "Disc successfully updated!"

class DeleteDisc(DeleteView):
    model = Disc
    template_name = "api/disc/delete_disc.html"
    success_url = reverse_lazy("api:disc_list")

# LIKE

class LikeList(ListView):
    model = Like
    template_name = "api/like/like_list.html"

    def get_queryset(self):
        queryset = Like.objects.all()
        search_query = self.request.GET.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(id__icontains=search_query) |
                Q(user__username__icontains=search_query) |
                Q(song__title__icontains=search_query)
            )
        return queryset

class LikeDetail(DetailView):
    model = Like
    template_name = "api/like/like_detail.html"

class CreateLike(SuccessMessageMixin, CreateView):
    model = Like
    form_class = CreateLikeForm
    template_name = "api/like/create_like.html"
    success_url = reverse_lazy("api:like_list")
    success_message = "Like successfully created!"

class UpdateLike(SuccessMessageMixin, UpdateView):
    model = Like
    form_class = CreateLikeForm
    template_name = "api/like/update_like.html"
    success_url = reverse_lazy("api:like_list")
    success_message = "Like successfully updated!"

class DeleteLike(DeleteView):
    model = Like
    template_name = "api/like/delete_like.html"
    success_url = reverse_lazy("api:like_list")
