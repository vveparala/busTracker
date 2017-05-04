# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Record(models.Model):
    user=models.CharField(max_length=20)
    json_str=models.TextField()
    ts=models.DateTimeField(auto_now_add=True)
