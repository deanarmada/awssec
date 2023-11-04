"""hacksite_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from blog.views import index
from authentication.views import register, login, change_password


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('change-password/', change_password, name='change-password'),
    path('change-password/<pk>', change_password),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', index, name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
