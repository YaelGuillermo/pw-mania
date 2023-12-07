from django.contrib import admin
from django.urls import path
from main import views
from api import views as apiview

app_name = 'main'

urlpatterns = [
    ### General ####
    path('' , views.SignupPage , name='signup'),
    path('login/' , views.LoginPage , name='login'),
    path('search/',views.SearchList , name='search'),
    path('album/list/', views.AlbumList, name='album_list'),
    path('api/developer_menu' , views.AdminPage , name='developer_menu'),
    path('like/list/' , views.LikeList , name='like_list'),
    path('like/create/' , views.CreateLike , name='create_like'),
    path('logout/' , views.LogoutPage , name='logout'),
    
    ### Info ###
    path('profile/', views.ProfileDetail, name='profile'),
    path('profile/update/', views.UpdateProfile, name='update_profile'),
    path('artist/detail/<int:pk>/', views.ArtistDetail, name='artist_detail'),
    path('genre/detail/<int:pk>/', views.GenreDetail, name='genre_detail'),
    path('album/detail/<int:pk>/', views.AlbumDetail, name='album_detail'),
    path('country/detail/<int:pk>/', views.CountryDetail, name='country_detail'),
    
    ### PlayList ###
    path('playlist/list/', views.PlaylistList, name="playlist_list"),
    path('playlist/detail/<int:pk>/', views.PlaylistDetail, name="playlist_detail"),
    path('playlist/create/', views.CreatePlaylist, name="create_playlist"),
    path('playlist/update/<int:pk>/', views.UpdatePlaylist, name="update_playlist"),
    path('playlist/delete/<int:pk>/', views.DeletePlaylist, name="delete_playlist"),

    ### Disc ###
    path('disc/list/', views.DiscList, name="disc_list"),
    path('Disc/<int:pk>/', views.DiscDetail, name="disc_detail"),
    path('Disc/create/', views.CreateDisc, name="create_disc"),
    path('Disc/update/<int:pk>/', views.UpdateDisc, name="update_disc"),
    path('Disc/delete/<int:pk>/', views.DeleteDisc, name="delete_disc"),
]
