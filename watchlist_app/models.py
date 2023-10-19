from django.db import models
from taggit.managers import TaggableManager
from django.core.validators import MinValueValidator, MaxValueValidator
# import USER
from django.contrib.auth.models import User

class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
# Create your models here.
class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
     # Create Django Relationships
    streamingPlatform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True) 
    created = models.DateTimeField(auto_now_add=True) 
    tags = TaggableManager()
    #Add the Image Field N give the default path to store the image
    image = models.ImageField(upload_to='Images/', default="Images/None/Noimg.jpg")

   
    def __str__(self):
        return self.title
    
# Create a New Model "Review"
class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    # 1 movie can have many reviews
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.rating) + " ----" +self.watchlist.title
