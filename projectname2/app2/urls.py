from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('', homePage, name='home_page'),
    path('posts/<str:slug>/', detailPage, name='detail_page'),
    path('posts/category/<str:slug>/', category, name='category'),
    path('abouts/', aboutPage, name='about_page'),
    path('contact/', contactPage, name='contact_page'),
    path('login/', Login , name='login'),
    path('login-process/', loginProcess, name='login_process'),
    path('logout/', logoutProcess, name='logout'),
    path('register/',  registerPage, name='register'),
    path('blog-author-page.html', TemplateView.as_view(template_name='blog-author-page.html'), name='blog_author_page'),
    
    
    
    
    
    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
    
    path('reset_password_sent/',
      auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
     
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
        
      
    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),
        

]