# from django.contrib import admin
# from .models import Skill,Project

# # Register your models here
# admin.site.register(Skill)
# admin.site.register(Project)

from django.contrib import admin
from .models import Skill, Project

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "iconUrl")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "preview")
    filter_horizontal = ("skills",)  # 👈 This enables multi-select list for skills
