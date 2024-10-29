from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from django.http import request


# Create your views here.
class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 2

    def get_paginate_by(self, queryset):
        paginate_by = self.request.GET.get('paginate_by', self.paginate_by)
        return int(paginate_by) if str(paginate_by).isdigit() else self.paginate_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paginate_by'] = self.get_paginate_by(self.get_queryset())
        return context



