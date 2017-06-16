from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import Post
from .forms import ContactForm

# Create your views here.
def post1(request, id):
    post=Post.objects.get(id=id)

    return render(request, 'blog/post1.html', {'p':'Dragon Ball Z sagas','cabeza':'mi blog','post': post})

def post_list(request):
    posts = Post.objects.all()

    return render(request, 'blog/post_list.html', {'p': 'Dragon Ball z sagas','cabeza':'mi blog', 'posts': posts})

def gracias(request):
    

    return render(request,"blog/gracias.html")


def contacto(request):
	if request.method== "POST":
		form= ContactForm(request.POST)
		if form.is_valid():

			return redirect ("/gracias")
	else:
		form= ContactForm()
	return render(request,"blog/contacto.html",{"form":form})

   
