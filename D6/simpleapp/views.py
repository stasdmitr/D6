from django.shortcuts import render
from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import News


class NewsList(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 1


class NewsDetail(DetailView):
    model = News
    template_name = 'concrete_News.html'
    context_object_name = 'news'
