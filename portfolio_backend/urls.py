"""
URL configuration for portfolio_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from skillsProjects.views import SkillViewSet,ProjectViewSet
from django.conf.urls.static import static
from .import settings,views


router = DefaultRouter()
router.register(r'skills', SkillViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhook', views.github_webhook, name='github_webhook'), # auto trigger whenver code push on git
    path('',include(router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
