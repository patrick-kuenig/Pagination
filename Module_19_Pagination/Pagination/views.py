from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from django.http import request


# Create your views here.
class IndexView(ListView):
    model = Post
    template_name = 'index.html'

    def get_paginate_by(self, queryset):
        if self.request.GET.get('paginate_by', self.paginate_by) is None:
            return 2
        else:
            return self.request.GET.get('paginate_by', self.paginate_by)



