# -*- coding: utf-8 -*-

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    new_photo = models.ImageField(upload_to='photos', null=True, blank=True)

    def __str__(self):
        return self.title
