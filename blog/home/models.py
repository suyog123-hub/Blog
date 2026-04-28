from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # this helps to avoid creating the sepearate table in the database 
    class Meta:
        abstract = True


class BlogPost(BaseModel):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=200)
    content = models.TextField()




    def __str__(self):
        return self.title