# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms import PasswordInput
# Create your models here.
from django import forms

class Traffic(models.Model):
	Route = models.CharField(max_length=50)
	Density = models.IntegerField(default=170)
	Date = models.DateField(null=True)

class OverSpeed(models.Model):
	Route = models.CharField(max_length=50)
	Speed = models.IntegerField(default=170)
	Date = models.DateField(null=True)
	Vehiclenum = models.CharField(max_length=50)	

