from django.db import models

class Contact(models.Model):
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject