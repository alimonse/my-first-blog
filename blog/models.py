from django.db import models # almacena en models
from django.utils import timezone

class Post(models.Model): # crea objeto post que tiene autor titulo texto
    author = models.ForeignKey('auth.User') #clave foranea
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)      #time.now fecha actual
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title #devuelve el titulo del post que le llame
# Create your models here.
#un modelo es la representacion en la base de datos
