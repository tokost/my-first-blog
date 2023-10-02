from django.shortcuts import render
from django.utils import timezone   # pridane v kapitole 13
from .models import Post    # pridane v kapitole 13

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')  # pridane v kapitole 13
    return render(request, 'blog/post_list.html', {'posts': posts})    # pridane a doplnene v kap. 13

