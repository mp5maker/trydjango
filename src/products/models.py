# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) # max_length is required
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=1000)
    summary     = models.TextField(default="Write Meaningful Description")
    ## Added After two products were added, featured was added
    featured    = models.BooleanField() # null=True, default=True

    ## Get Absolute Url using the string substitution