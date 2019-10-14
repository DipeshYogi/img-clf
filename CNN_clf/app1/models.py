from django.db import models

class ImgModel(models.Model):
    img = models.ImageField(upload_to='profile_pics', verbose_name='Profile pic')

    def __str__(self):
        return 'img'
