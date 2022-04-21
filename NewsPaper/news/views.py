from django.shortcuts import render

# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime

class NewsList(ListView):
   # model = Post
   # ordering = 'title'
   template_name = 'News.html'
   context_object_name = 'news'
   queryset = Post.objects.order_by('-dateCreation')

class NewsDetail(DetailView):
    model = Post
    template_name = 'onenews.html'
    context_object_name = 'onenews'
