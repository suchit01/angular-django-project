from django.db import models

# Create your models here.

class MoviesList(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, editable=False)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=800)
    release_date = models.DateField('Release date')
    num_actors = models.IntegerField(default=1)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def upvote(self, *args, **kwargs):
        self.upvotes = self.upvotes + 1
        super().save(*args, **kwargs)
    
    def downvote(self, *args, **kwargs):
        self.downvotes = self.downvotes + 1
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title

class ActorsList(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField('Date of Birth')
    num_movies = models.IntegerField(default=0)

    def __str__(self):
        return self.name