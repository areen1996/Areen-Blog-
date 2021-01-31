from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Category (models.Model):
    Title = models.CharField(max_length=100)
    #Description = models.TextField()

    def __str__(self):
        return self.Title 

    def get_absolute_url(self):
        #return reverse("model_detail", kwargs={"pk": self.pk})
        return reverse ('home')


class Article(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Publish_Date = models.DateTimeField(default=timezone.now)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    #Likes
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.Title + ' | '+ str(self.Author) 
 
    def get_absolute_url(self):
        #return reverse("model_detail", kwargs={"pk": self.pk})
        return reverse ('home')


