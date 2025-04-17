from django.shortcuts import render
from posts.models import *
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy

class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published = True)
    
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = ['title', 'content', 'published', 'author', 'thumbail', 'created_on']

class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_update.html"
    fields = ['title', 'content', 'published', 'author', 'thumbail', 'created_on']

class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"

class BlogPostDelete(DeleteView):
    model = BlogPost
    context_object_name = "post"
    success_url = reverse_lazy('posts:home')
    
# Create your views here.
