from django.db import models
import re
import datetime

def generate_slug(title):
    slug = re.sub(r'[^\w\s-]', '', title)
    slug = re.sub(r'\s+', '-', slug.lower())
    return slug

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(upload_to='blog_images/')  
    author_name = models.CharField(max_length=50, default="Author Name")
    author_image = models.ImageField(upload_to='blog_images/')

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:50] + '...'
