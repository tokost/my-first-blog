from django.db import models

# Create your models here.
from django.conf import settings  # vytvorenie modelu pre blog post
from django.utils import timezone


class Post(models.Model):  # definicia nasho modelu - je to objekt (podla class),
                            #  Post je meno a model.Model znamena ze je Django model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title  # koniec mojho mopdelu
