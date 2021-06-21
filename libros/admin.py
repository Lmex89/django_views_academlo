from django.contrib import admin

# Register your models here.
from libros.models import Libro,Editorial,Autor

admin.site.register(Libro)
admin.site.register(Editorial)
admin.site.register(Autor)