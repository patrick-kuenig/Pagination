from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.http import request


# Create your views here.
class IndexView(ListView):
    try:
        paginate_by = request.GET['dropdown']
    except:
        paginate_by = 1
    model = Post
    template_name = 'index.html'
