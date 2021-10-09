from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from user import views as user_views
from mail.views import MailListView

urlpatterns = [
        path('', MailListView.as_view(),name='home'),
        path('register/', user_views.register, name='register'),
        path('profile/', user_views.profile, name='profile'),
        path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
]
