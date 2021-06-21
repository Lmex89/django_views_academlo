from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=32)
    edad = models.IntegerField()
    fecha_de_publicacion = models.DateField()
    
    def __str__(self):
        return self.nombre

class Editorial(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    pagina_web = models.CharField(max_length=35)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    nombre = models.CharField(max_length=30)
    paginas = models.IntegerField()
    publicado = models.BooleanField()
    fecha_de_publicacion = models.DateField()
    editorial = models.ForeignKey(Editorial,
                                  null=True,
                                  blank=True,
                                  on_delete=models.SET_NULL)
    autores = models.ManyToManyField(Autor,
                                     related_name="libros")
    
    def __str__(self):
        return self.nombre
