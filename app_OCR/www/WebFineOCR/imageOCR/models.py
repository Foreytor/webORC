from django.db import models
from .validators import validate_file_extension
# Create your models here.

class ImageForOCR(models.Model):
    imageFile = models.ImageField(upload_to='img/%Y/%m/%d', validators=[validate_file_extension])
    
    
