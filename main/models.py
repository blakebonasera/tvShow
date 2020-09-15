from django.db import models

# Create your models here.
class Tv(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=20)
    release = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"{self.title} - {self.network} - {self.release} - {self.desc}"