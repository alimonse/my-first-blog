from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts}) #3 paramentosrequest siguiente , el parametro que queremos abrir, objeto vacio
    #traer en llaves lista avanzada 'algo' busca el algo en la lista



# Create your views here.
