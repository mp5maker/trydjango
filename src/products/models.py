# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) # max_length is required
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=1000)
    summary     = models.TextField(default="Write Meaningful Description")
    ## Added After two products were added, featured was added
    featured    = models.BooleanField() # null=True, default=True

    ## Get Absolute Url using the string substitution
    def get_absolute_url(self):
        # return f"/product/dynamic-lookup/{self.id}" # Better Way to url
        
        # This is going to use the name of the url
        return reverse("products:dynamic_lookup_view", kwargs={"product_id": self.id})
