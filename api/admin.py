from django.contrib import admin
from main.models import *

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["name", "abbreviation"]
    search_fields = ["name", "abbreviation"]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "calculate_age", "days_since_creation", "biography"]
    search_fields = ["user__username", "biography"]
    list_filter = ["created_at", "birth_date"]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name"]

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ["name", "nickname", "birth_date", "nationality"]
    search_fields = ["name", "nickname", "nationality__name"]
    list_filter = ["genres"]

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ["title", "date", "description"]
    search_fields = ["title"]
    list_filter = ["artists", "genres", "date"]

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ["title", "format_duration", "album"]
    search_fields = ["title", "album__title"]
    list_filter = ["genres"]

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "description"]
    search_fields = ["user__username", "title"]

@admin.register(Disc)
class DiscAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "format_duration"]
    search_fields = ["user__username", "title"]
    list_filter = ["genres"]

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ["user", "song"]
    search_fields = ["user__username", "song__title"]
