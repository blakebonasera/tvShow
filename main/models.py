from django.db import models

# Create your models here.
class TvManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Hey idiot what title is one character"
        if len(postData['network']) < 3:
            errors['network'] = "LOOK AT THIS FOOL! WHAT KIND OF NETWORK DO YOU THINK THAT IS?"
        if len(postData['description']) < 10:
            errors['description'] = "Very descriptive aren't ya??"
        return errors

class Tv(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=20)
    release = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TvManager()
    def __repr__(self):
        return f"{self.title} - {self.network} - {self.release} - {self.desc}"


