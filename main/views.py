from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from youtube_search import YoutubeSearch
import json
from django.http import JsonResponse
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

# Create your views here.
@login_required(login_url='login')
def AdminPage(request):
    return render (request,'api/developer_menu.html')

def SignupPage(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1!=pass2:
            error_message = "Your password's are not the same!!"
            return render(request, 'main/signup.html', {'error_message': error_message})
            #return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            profile = Profile(user=my_user)
            profile.save()
            return redirect('main:login')
    return render (request,'main/signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('api:developer_menu')
            else:
                return redirect('main:album_list') 
            #return redirect('home')
        else:
            error_message = "Username or Password is incorrect!!"
            return render(request, 'main/login.html', {'error_message': error_message})
            #return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'main/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('main:login')

@login_required
def ProfileDetail(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    context = {
        'user': user,
        'profile': profile,
    }

    return render(request, 'main/profile.html', context)

def UpdateProfile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # Redirect to the profile page or wherever you want
            return redirect('main:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'main/update_profile.html', {'user_form': user_form, 'profile_form': profile_form})

def ArtistDetail(request):
    artists = Artist.objects.all()
    return render(request, 'main/artist_detail.html', {'artists': artists})

def AlbumList(request):
    # Obtén todos los géneros disponibles
    genres = Genre.objects.all()
    albums = Album.objects.all()
    albums_by_genre = {}
    for genre in genres:
        albums_by_genre[genre.name] = Album.objects.filter(genres=genre)

    albums_with_song_ids = []
    for album in albums:
        song_ids = album.get_all_video_ids()
        albums_with_song_ids.append({'album': album, 'song_ids': song_ids})

    return render(request, 'main/album_list.html', {'albums_with_song_ids': albums_with_song_ids, 'albums_by_genre': albums_by_genre})
    #return render(request, 'main/album_list.html', {'albums_by_genre': albums_by_genre})

@login_required
def PlaylistList(request):
    playlists = Playlist.objects.filter(user=request.user)
    return render(request, 'main/playlist_list.html', {'playlists': playlists})

def CreatePlaylist(request):
    if request.method == 'POST':
        playlist_form = PlaylistCreateForm(request.POST, request.FILES)

        if playlist_form.is_valid():
            playlist = playlist_form.save(commit=False)
            playlist.user = request.user
            playlist.save()
            playlist_form.save_m2m()
            return redirect('main:playlist_list')
    else:
        playlist_form = PlaylistCreateForm()

    return render(request, 'main/create_playlist.html', {'playlist_form': playlist_form})


def PlaylistDetail(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk)
    return render(request, 'main/playlist_detail.html', {'playlist': playlist})

def UpdatePlaylist(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk)

    if request.method == 'POST':
        playlist_form = PlaylistCreateForm(request.POST, request.FILES, instance=playlist)
        if playlist_form.is_valid():
            playlist = playlist_form.save()
            return redirect('main:playlist_detail', pk=pk)
    else:
        playlist_form = PlaylistCreateForm(instance=playlist)

    return render(request, 'main/update_playlist.html', {'playlist_form': playlist_form, 'playlist': playlist})

def DeletePlaylist(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk)

    if request.method == 'POST':
        playlist.delete()
        return redirect('main:playlist_list')

    return render(request, 'main/delete_playlist.html', {'playlist': playlist})


@login_required
def DiscList(request):
    discs = Disc.objects.filter(user=request.user)
    return render(request, 'main/disc_list.html', {'discs': discs})

def CreateDisc(request):
    if request.method == 'POST':
        disc_form = DiscCreateForm(request.POST, request.FILES)

        if disc_form.is_valid():
            disc = disc_form.save(commit=False)
            disc.user = request.user
            disc.save()
            disc_form.save_m2m()
            return redirect('main:disc_list')
    else:
        disc_form = DiscCreateForm()

    return render(request, 'main/create_disc.html', {'disc_form': disc_form})


def DiscDetail(request, pk):
    disc = get_object_or_404(Disc, pk=pk)
    return render(request, 'main/disc_detail.html', {'disc': disc})

def UpdateDisc(request, pk):
    disc = get_object_or_404(Disc, pk=pk)

    if request.method == 'POST':
        disc_form = DiscCreateForm(request.POST, request.FILES, instance=disc)
        if disc_form.is_valid():
            disc = disc_form.save()
            return redirect('main:disc_list')
    else:
        disc_form = DiscCreateForm(instance=disc)

    return render(request, 'main/update_disc.html', {'disc_form': disc_form, 'disc': disc})

def DeleteDisc(request, pk):
    disc = get_object_or_404(Disc, pk=pk)

    if request.method == 'POST':
        disc.delete()
        return redirect('main:disc_list')

    return render(request, 'main/delete_disc.html', {'disc': disc})

def AlbumDetail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'main/album_detail.html', {'album': album})

def GenreDetail(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    artists_in_genre = Artist.objects.filter(genres=genre)
    albums_in_genre = Album.objects.filter(genres=genre)
    return render(request, 'main/genre_detail.html', 
                  {'genre': genre, 
                   'artists_in_genre': artists_in_genre,
                   'albums_in_genre': albums_in_genre})

def ArtistDetail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'main/artist_detail.html', {'artist': artist})

def CountryDetail(request, pk):
    country = get_object_or_404(Country, pk=pk)
    artists_in_country = Artist.objects.filter(nationality=country)
    return render(request, 'main/country_detail.html', {'country': country, 'artists_in_country': artists_in_country})

@login_required
def LikeList(request):
    liked_songs = Like.objects.filter(user=request.user)
    return render(request, 'main/like_list.html', {'likes': liked_songs})

@csrf_exempt
def CreateLike(request):
    if request.method == 'POST':
        user_id = request.POST.get('user')
        song_id = request.POST.get('song')
        Like.objects.create(user_id=user_id, song_id=song_id)

        return JsonResponse({'message': 'Like guardado con éxito'})
    else:
        return JsonResponse({'message': 'Método no permitido'}, status=405)

def SearchList(request):
    template_name = 'main/search.html'
    query = request.GET.get('q', '')

    # Buscar en Genre por su name
    genres = Genre.objects.filter(name__icontains=query)

    # Buscar en Artist por name, nickname, nationality, genres
    artists = Artist.objects.filter(
        Q(name__icontains=query) | Q(nickname__icontains=query) |
        Q(nationality__name__icontains=query) | Q(genres__name__icontains=query)
    ).distinct()

    # Buscar en Album por title, artists, genres
    albums = Album.objects.filter(
        Q(title__icontains=query) | Q(artists__name__icontains=query) |
        Q(genres__name__icontains=query)
    ).distinct()

    # Buscar en Song por title, genres, album
    songs = Song.objects.filter(
        Q(title__icontains=query) | Q(genres__name__icontains=query) |
        Q(album__title__icontains=query)
    ).distinct()

    context = {
        'query': query,
        'genres': genres,
        'artists': artists,
        'albums': albums,
        'songs': songs,
    }

    return render(request, template_name, context)
