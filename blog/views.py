from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

from .models import Binta

def post_list(request):
    posts = Binta.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Binta, pk=id)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})