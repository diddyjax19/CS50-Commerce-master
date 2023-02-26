# All relevant imports
# References: < Havrard CS50 and Zach Barlow> 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django import forms
# Handles client side Error exceptions
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError