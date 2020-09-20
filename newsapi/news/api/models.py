from django.db import models

class Article(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=250)
    body = models.TextField()
    location = models.CharField(max_length=120)
    publication_data = models.DateField()
    active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}{self.title}"
