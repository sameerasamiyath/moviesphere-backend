from django.db import models


# =========================
# GENRE MODEL
# =========================
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# =========================
# MOVIE MODEL
# =========================
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    language = models.CharField(max_length=100)
    is_premium = models.BooleanField(default=False)

    video_url = models.URLField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title