from django.contrib import admin

from .models import Image,Clases,Alumno,Profesor,Admin,Embedding

# Register your models here.
admin.site.register(Image)
admin.site.register(Clases)
admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Admin)
admin.site.register(Embedding)