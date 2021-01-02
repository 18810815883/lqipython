from django.shortcuts import render
from django.http import  HttpResponse
from .models import Homework,Student
from django.views.generic.edit import CreateView
# Create your views here.

class HomeworkCreate(CreateView): 
    model = Homework 
    template_name = 'homework_form.html' 
    fields = ['headline','attach','remark','student']
    
  