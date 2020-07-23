from django.db import models
from django.contrib.auth.models import User

class Setting (models.Model):
    user_id = models.OneToOneField(User, blank=True, on_delete = models.CASCADE)
    name = models.CharField('Nombres',max_length=200, null=True)
    phone = models.CharField('Telefono',max_length=200, null=True)
    description = models.TextField('Descripcion', null=True)
    image = models.ImageField('Imagen',default="logo.png", null=True, blank=True)
    date_setting = models.DateTimeField(auto_now_add=True, null=True)
    
    

    class Meta:
        verbose_name = 'Cofiguracion'
        verbose_name_plural = 'Cofiguraciones'
        ordering = ['date_setting']

    def __str__(self):
        return self.name
    

  
