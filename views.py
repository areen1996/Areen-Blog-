from django.shortcuts import render 
from django.views.generic import ListView , DetailView 
from .models import Article , Category

#def home(request):
#   return render(request , 'home.html' ,{})


class Homeview(ListView):
    model = Article
    template_name = 'home.html'



class Describtion(DetailView):
    model= Article
    template_name= 'describtion.html'


class Categoryview(ListView):
    model = Category
    template_name = "category.html"