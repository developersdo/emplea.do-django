#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Los modelos creados!
from django.template.defaultfilters import slugify
from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categorías"

    name = models.CharField(max_length=30, verbose_name="nombre")
    slug = models.SlugField(max_length=30)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return ("category/%s" % self.slug)

class Job(models.Model):
    name = models.CharField(max_length=200, verbose_name="nombre del trabajo")
    category = models.ForeignKey(Category, verbose_name="categoría")
    place = models.CharField(max_length=200, verbose_name="lugar")
    description = models.TextField(verbose_name="Perfil de puesto")
    application = models.TextField(verbose_name="Como aplicar?")
    pub_date = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(max_length=200, verbose_name="nombre de compañía")
    url = models.URLField(blank=True, null=True)
    email = models.EmailField()
    logo = models.ImageField(upload_to="images/logos", blank=True, null=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return ("/job/%i/" % self.id)


#class Company(models.Model):
#    name = models.CharField(max_length=200, verbose_name="nombre de compañía")
#    slug = models.SlugField(max_length=200)
#    url = models.URLField()
#    email = models.EmailField()
#    logo = models.ImageField(upload_to="images/logos")
    
#    def __unicode__(self):
#        return self.name
    



