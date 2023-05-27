from os import name
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from taggit.managers import TaggableManager
import django_filters


# Create your models here.
# Create your models here.
BLOG_CATEGORIES = [
    ('', ''),
    ('tech', 'tech'),
    ('sports','sports'),
    ('news' , 'news'),
    ('education' , 'education'),
]
STATUS = [
    ('draft', 'draft'),
    ('published','published'),
]

class Category(models.Model):
  name = models.CharField(max_length=200, default= None, blank=True, null=True)
  slug = models.SlugField(blank= True, null= True) 

  def __str__(self):
    return str(self.name)


class PostAuthor(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 full_name = models.CharField(max_length=200, default= None, blank=True, null=True)
 image = models.ImageField(upload_to= 'authors/imhes/', blank= True , null= True)
 email = models.EmailField()
 phone_message = "Phone no must be entered in the format of 03479999999"

 #your desired format
 phone_regex = RegexValidator(
    regex=r'^(05)\d{9}$ ',
     message=phone_message
       )
 phone_number = models.CharField(max_length=60,null=True, blank=True)
 facebook = models.URLField(default=None, blank=True)
 twitter = models.URLField(default=None, blank=True)
 instagram = models.URLField(default=None, blank=True)
 linkedin = models.URLField(default=None, blank=True)
 slug = models.SlugField(blank= True, null= True)

def __str__(self):
  return self.full_name

def save(self, *args, **kwargs):
   if not self.slug and self.full_name:
     self.slug = slugify(self.full_name)
   super(PostAuthor,self).save(*args, **kwargs)
class Meta:
  verbose_name= 'Blog Post Author'
  verbose_name_plural= 'Blog Post Author'


class Post(models.Model):
 title = models.CharField(max_length=200, default=None, null=False)
 description = models.TextField()
 image = models.ImageField(default=None, upload_to="pictures/uni.jpg" )
 published_time= models.DateTimeField(auto_now_add=True)
 category = models.ForeignKey(Category, on_delete=models.CASCADE)
 status = models.CharField(max_length=200, default='draft', choices=STATUS)
 author = models.ForeignKey(PostAuthor, on_delete=models.CASCADE, null=True)
 slug = models.SlugField(blank= True, null= True)

 def save(self, *args, **kwargs):
   if not self.slug and self.title:
     self.slug = slugify(self.title)
   super(Post,self).save(*args, **kwargs)
 
 def __str__(self):
  return self.title
    