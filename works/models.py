from django.db import models

class Work(models.Model):
    imagesrc = models.ImageField(upload_to='static/works/')
    url = models.URLField(blank=True)
    flag = models.BooleanField(blank=True)
    titleno = models.CharField(max_length=10)
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.title

