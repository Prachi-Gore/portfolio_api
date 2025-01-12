from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
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
      filter_backends = [DjangoFilterBackend]
      filterset_fields = {
        'skills': ['in'],  # Use 'in' for filtering by multiple skill IDs
    }

      def get_queryset(self):
        queryset = super().get_queryset()
        skills_param = self.request.query_params.get('skills', None)
        if skills_param:
            # Split the skills parameter into a list of UUIDs
            try:
                skill_ids = skills_param.split(',')
                queryset = queryset.filter(skills__id__in=skill_ids).distinct()
            except ValueError:
                raise ValidationError({'skills': 'Invalid format for skills. Use a comma-separated list of UUIDs.'})
        return queryset