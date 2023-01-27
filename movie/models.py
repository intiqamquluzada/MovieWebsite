from django.db import models
from services.categories import CHOICES
from services.uploader import Uploader
from services.mixin import DateMixin, SlugMixin
from services.generator import Generator
from django.core.validators import MinValueValidator, MaxValueValidator
from services.place import PLACES


class Cast_of_Movie(SlugMixin, DateMixin):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=Uploader.upload_images_for_cast)
    position = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Cast_of_Movie)
        super(Cast_of_Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Movie(DateMixin, SlugMixin):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=CHOICES)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    image = models.ImageField(upload_to=Uploader.upload_images_to_movies)
    place = models.CharField(max_length=200, choices=PLACES, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    people = models.ForeignKey(Cast_of_Movie, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Movie)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} --> movie"

    class Meta:
        ordering = ("-created_at",)
