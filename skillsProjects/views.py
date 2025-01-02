from django.shortcuts import render
from rest_framework import viewsets
from .models import Skill,Project
from .serializers import SkillSerializer,ProjectSerializer

# Create your views here.

class SkillViewSet(viewsets.ModelViewSet):
      queryset=Skill.objects.all()
      serializer_class=SkillSerializer

class ProjectViewSet(viewsets.ModelViewSet):
      queryset=Project.objects.all()
      serializer_class=ProjectSerializer