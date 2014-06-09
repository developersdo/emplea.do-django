from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __unicode__(self):
        return self.name

class Job(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, verbose_name="category")
    place = models.CharField(max_length=200)
    description = models.TextField()
    applies = models.TextField()
    pub_date = models.DateTimeField(auto_add_now=True)

    def __unicode__(self)
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    url = models.URLField()
    email = models.EmailField()
    logo = models.ImageField(upload_to=images/logos)
    
   def __unicode__(self):
       return self.name
    



