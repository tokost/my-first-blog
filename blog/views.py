from django.shortcuts import render
from django.utils import timezone  # pridane ako druhe
from .models import Post  # pridany riadok ako prvy
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')  # pridane druhe
    return render(request, 'blog/post_list.html', {'posts': posts})  # logika nasej aplikacie
