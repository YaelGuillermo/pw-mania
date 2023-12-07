from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta, datetime
from urllib.parse import urlparse, parse_qs

class Country(models.Model):
    name = models.CharField(max_length=30)
    abbreviation = models.CharField(max_length=2)
    image = models.ImageField(upload_to='countries', null=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    biography = models.TextField(max_length=180, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='profiles', null=True)
    def calculate_age(self):
        if self.birth_date:
            today = date.today()
            age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
            return age
        return None
    
    def days_since_creation(self):
        if self.created_at:
            today = datetime.now().date()
            days_since_creation = (today - self.created_at.date()).days
            return days_since_creation
        return None

    def __str__(self):
        return self.user.username

class Genre(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=180, blank=True)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to="artists", null=True)
    description = models.TextField(max_length=180, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.ForeignKey(Country, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)

    def calculate_age(self):
        if self.birth_date:
            today = date.today()
            age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
            return age
        return None

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=30)
    artists = models.ManyToManyField(Artist)
    genres = models.ManyToManyField(Genre)
    date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to="albums")
    description = models.TextField(blank=True)

    def get_all_video_ids(self):
        song_ids = [song.get_video_id() for song in self.song_set.all()]
        return song_ids

    def __str__(self):
        return self.title
    
class Song(models.Model):
    title = models.CharField(max_length=30)
    genres = models.ManyToManyField(Genre)
    duration = models.TimeField() #models.Duration()
    video = models.CharField(max_length=90)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def format_duration(self):
        hours, minutes, seconds = self.duration.hour, self.duration.minute, self.duration.second
        return f"{minutes:02d}:{seconds:02d} min."
    
    def get_video_id(self):
        try:
            parsed_url = urlparse(self.video)
            video_id = parse_qs(parsed_url.query).get('v')
            
            if video_id:
                return video_id[0]
            elif 'youtu.be' in parsed_url.netloc:
                return parsed_url.path[1:]
            else:
                return None
        except IndexError:
            return None
    
    def __str__(self):
        return self.title

class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    songs = models.ManyToManyField(Song)
    description = models.TextField(max_length=180, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Playlist: {self.name}"

class Disc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    genres = models.ManyToManyField(Genre)
    duration = models.DurationField()
    video = models.CharField(max_length=90)

    def format_duration(self):
        hours, minutes, seconds = self.duration.hour, self.duration.minute, self.duration.second
        return f"{minutes:02d}:{seconds:02d} min."
    
    def get_video_id(self):
        try:
            parsed_url = urlparse(self.video)
            video_id = parse_qs(parsed_url.query).get('v')
            
            if video_id:
                return video_id[0]
            elif 'youtu.be' in parsed_url.netloc:
                return parsed_url.path[1:]
            else:
                return None
        except IndexError:
            return None

    def __str__(self):
        return f"{self.user.username}'s Disc: {self.title}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} likes {self.song.title}"