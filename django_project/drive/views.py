from django.shortcuts import render
from django.http import HttpResponseRedirect #
from .models import Post
from rest_framework import viewsets #
from drive.serializers import DriveSerializer #
from django.contrib.auth.models import User #
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#class DriveViewSet(viewsets.ModelViewSet): #
#    queryset = User.objects.all()
#    serializer_class = DriveSerializer

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'drive/home.html', context)
	
class PostListView(ListView):
    model = Post
    template_name = 'drive/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
	
class PostDetailView(DetailView):
    model = Post
	
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author :
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author :
            return True
        return False	


def about(request):
    return render(request, 'drive/about.html', {'title': 'About'})

