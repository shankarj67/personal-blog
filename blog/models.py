from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField(max_length=150)
    body = models.TextField(max_length=255)
    publish_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

        
