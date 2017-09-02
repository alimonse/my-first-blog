from django.contrib import admin
from .models import Post
#si no tienes el cdm con el servidor toca levantar otra vez y despues 127.0.0.1:8000/admin
admin.site.register(Post)
# Register your models here.
