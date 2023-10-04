from django.shortcuts import render
from django.utils import timezone   # pridane v kapitole 13
from .models import Post            # pridane v kapitole 13
         
from django import forms            # zmenene
from .forms import PostForm         # pridane v kapitole 18

from django.shortcuts import redirect   # pridane v kapitole 18
from django.shortcuts import get_object_or_404

# Create your views here.
def post_list(request):     # pridane v kapitole 13
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')  
    return render(request, 'blog/post_list.html', {'posts': posts})    # pridane a doplnene v kap. 13

def post_new(request):      # pridane v kapitole 18
    if request.method == "POST":        
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:    
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

#what you see when you click on a post - posledmne pridane
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

