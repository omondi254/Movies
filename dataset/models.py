from django.db import models


# Create your models here.


class Movies(models.Model):
    CATEGORY_CHOICES = (
        ('SF', 'Science Fiction'),
        ('TH', 'Thriller'),
        ('AC', 'Action'),
        ('HO', 'Horror'),
        ('AD', 'Adventure'),
        ('RM', 'Romance'),
        ('AN', 'Animation'),
        ('MS', 'Music'),

    )

    class Meta:
        verbose_name_plural = "Movies"


    title = models.CharField(max_length=255)
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title
