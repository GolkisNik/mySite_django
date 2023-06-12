from django.db import models


# Create your models here.
class Articles(models.Model):
    title=models.CharField('Назва', max_length=50, default='')
    anons=models.CharField('Анонс', max_length=250,default='')
    full_text=models.TextField('Саття')
    date=models.DateTimeField('дата публікації')

  
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Новини'
        verbose_name_plural='Новини'
    