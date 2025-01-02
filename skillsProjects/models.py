from django.db import models
import uuid
# Create your models here.
class Skill(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=40)
    iconUrl=models.CharField(max_length=100)

    def __str__(self):
       return self.name

class Project(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField()
    src = models.FileField(upload_to='projects/videos/', null=True, blank=True)  # For video file path
    code = models.URLField(max_length=400)  # For GitHub or project code link
    preview = models.URLField(max_length=400)  # For live project preview link
    skills=models.ManyToManyField(Skill,related_name='projects')

    def __str__(self):
        return self.name