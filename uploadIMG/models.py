# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Images(models.Model):
	title_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	img_url = models.CharField(max_length=500)
	
