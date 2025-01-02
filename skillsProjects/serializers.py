from rest_framework import serializers
from .models import Skill,Project

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skill
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)  # Nested serializer for skills
    class Meta:
        model=Project   
        fields = '__all__'     