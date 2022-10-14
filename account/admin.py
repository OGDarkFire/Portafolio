from django.contrib import admin
from .models import User, Unidad,Rol,Usuario,Tarea,TareaSub

# Register your models here.
admin.site.register(User)
admin.site.register(Unidad)
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Tarea)
admin.site.register(TareaSub)