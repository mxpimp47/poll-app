from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    posts = Post.objects.filter(published=True)  # published posts
    return render(request, 'blog/index.html', {'posts': posts})


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)  # get post
    return render(request, 'blog/post.html', {'post': post})
