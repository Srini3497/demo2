from django.db import models
from django import forms

# Create your models here.
class FileUpload(models.Model):
    name = models.CharField(max_length=50)
    dp_pic = models.FileField(upload_to="media")

class FileForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = "__all__"
