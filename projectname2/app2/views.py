from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db.models import Q
# Create your views here.

# @login_required(login_url='login')
def homePage(request):
    data = Post.objects.filter(status='published').order_by("-published_time")

    search_query = request.GET.get('query')
    if search_query:
        data = data.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains= search_query)
        )
    context = {'data': data}
    return render(request, 'index.html', context)

def detailPage(request, slug):
    data = get_object_or_404(Post, slug=slug)
    context = {'data': data}
    return render(request, 'post.html', context)

def aboutPage(request):
    data = Post.objects.first()
    context = {'data': data}
    return render(request, 'about.html', context)

def contactPage(request):
    if request.method == 'POST':
        email = EmailMessage(
            request.POST.get('name'),
            request.POST.get('phone'),
            request.POST.get('message'),
            request.POST.get('email'),
            settings.EMAIL_HOST_USER,
            ['namrahali222@gmail.com']
        )
        email.send()
        return redirect("home_page")
    return render(request, 'contact.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was sreated for' + user)
                
                return redirect('login')
            
        context = {'form': form}
        return render(request, 'signup.html', context)
        
def Login(request):
    return render(request, 'login.html')

def loginProcess(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    print(username, password)
    
    user = authenticate(request=request, username=username, password=password)
    if user is not None:
        login(request=request, user=user)
        messages.success(request, "Login Successful")
        return HttpResponseRedirect(reverse("home_page"))
    else:
        messages.error(request, "Error in login! Invalid Login Details!")
        return HttpResponseRedirect(reverse("login"))

def logoutProcess(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return HttpResponseRedirect(reverse("login"))



def user_articles(request,slug):
     authordetail = PostAuthor.objects.get(slug=slug)
     articles = Post.objects.filter(status= 'published', author= authordetail)
     count = articles.count()
     return render(request, "blog-author-page.html",{'articles': articles,'authordetail':authordetail,'count':count})


def category(request,slug):
     categorydetail = Category.objects.get(slug=slug)
     articles = Post.objects.filter(status= 'published', category= categorydetail)
     count = articles.count()
     return render(request, "blog-category-page.html",{'articles': articles,'categorydetail':categorydetail,'count':count})