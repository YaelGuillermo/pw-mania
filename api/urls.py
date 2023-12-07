from django.urls import path
from api import views

app_name = "api"

urlpatterns = [
    ### Menu ###
    path('', views.DeveloperMenuView.as_view(), name="developer_menu"),

    #### User ####
    path('users/', views.UserList.as_view(), name="user_list"),
    path('users/<int:pk>/', views.UserDetail.as_view(), name="user_detail"),
    path('users/create/', views.CreateUser.as_view(), name="create_user"),   
    path('users/update/<int:pk>/', views.UpdateUser.as_view(), name="update_user"),
    path('users/delete/<int:pk>/', views.DeleteUser.as_view(), name="delete_user"),
    
    #### Artist ####
    path('artists/', views.ArtistList.as_view(), name="artist_list"),
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name="artist_detail"),
    path('artists/create/', views.CreateArtist.as_view(), name="create_artist"),
    path('artists/update/<int:pk>/', views.UpdateArtist.as_view(), name="update_artist"),
    path('artists/delete/<int:pk>/', views.DeleteArtist.as_view(), name="delete_artist"),

    #### Profile ####
    path('profiles/', views.ProfileList.as_view(), name="profile_list"),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view(), name="profile_detail"),
    path('profiles/update/<int:pk>/', views.UpdateProfile.as_view(), name="update_profile"),

    #### Country ####
    path('countries/', views.CountryList.as_view(), name="country_list"),
    path('countries/<int:pk>/', views.CountryDetail.as_view(), name="country_detail"),
    path('countries/create/', views.CreateCountry.as_view(), name="create_country"),
    path('countries/update/<int:pk>/', views.UpdateCountry.as_view(), name="update_country"),
    path('countries/delete/<int:pk>/', views.DeleteCountry.as_view(), name="delete_country"),

    #### Genre ####
    path('genres/', views.GenreList.as_view(), name="genre_list"),
    path('genres/<int:pk>/', views.GenreDetail.as_view(), name="genre_detail"),
    path('genres/create/', views.CreateGenre.as_view(), name="create_genre"),
    path('genres/update/<int:pk>/', views.UpdateGenre.as_view(), name="update_genre"),
    path('genres/delete/<int:pk>/', views.DeleteGenre.as_view(), name="delete_genre"),

    #### Album ####
    path('albums/', views.AlbumList.as_view(), name="album_list"),
    path('albums/<int:pk>/', views.AlbumDetail.as_view(), name="album_detail"),
    path('albums/create/', views.CreateAlbum.as_view(), name="create_album"),
    path('albums/update/<int:pk>/', views.UpdateAlbum.as_view(), name="update_album"),
    path('albums/delete/<int:pk>/', views.DeleteAlbum.as_view(), name="delete_album"),

    #### Song ####
    path('songs/', views.SongList.as_view(), name="song_list"),
    path('songs/<int:pk>/', views.SongDetail.as_view(), name="song_detail"),
    path('songs/create/', views.CreateSong.as_view(), name="create_song"),
    path('songs/update/<int:pk>/', views.UpdateSong.as_view(), name="update_song"),
    path('songs/delete/<int:pk>/', views.DeleteSong.as_view(), name="delete_song"),

    #### Playlist ####
    path('playlists/', views.PlaylistList.as_view(), name="playlist_list"),
    path('playlists/<int:pk>/', views.PlaylistDetail.as_view(), name="playlist_detail"),
    path('playlists/create/', views.CreatePlaylist.as_view(), name="create_playlist"),
    path('playlists/update/<int:pk>/', views.UpdatePlaylist.as_view(), name="update_playlist"),
    path('playlists/delete/<int:pk>/', views.DeletePlaylist.as_view(), name="delete_playlist"),

    #### Disc ####
    path('discs/', views.DiscList.as_view(), name="disc_list"),
    path('discs/<int:pk>/', views.DiscDetail.as_view(), name="disc_detail"),
    path('discs/create/', views.CreateDisc.as_view(), name="create_disc"),
    path('discs/update/<int:pk>/', views.UpdateDisc.as_view(), name="update_disc"),
    path('discs/delete/<int:pk>/', views.DeleteDisc.as_view(), name="delete_disc"),

    #### Like ####
    path('likes/', views.LikeList.as_view(), name="like_list"),
    path('likes/<int:pk>/', views.LikeDetail.as_view(), name="like_detail"),
    path('likes/create/', views.CreateLike.as_view(), name="create_like"),
    path('likes/update/<int:pk>/', views.UpdateLike.as_view(), name="update_like"),
    path('likes/delete/<int:pk>/', views.DeleteLike.as_view(), name="delete_like"),
]

