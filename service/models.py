from django.db import models

# Create your models here.

class DhuiFace(models.Model):
    action = models.CharField(verbose_name='动作', max_length=50, null=False, blank=False)
    faceid = models.CharField(verbose_name='人脸编号', max_length=50, unique=True, null=False, blank=False)
    base64 = models.CharField(verbose_name='人脸照片', max_length=200, null=False, blank=False)

    def __str__(self):
        return self.action

