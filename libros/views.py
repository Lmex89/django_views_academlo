from libros.models import Autor
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def get_autores(request):
    
    autores_queryset = Autor.objects.all()
    #lista_autores_str =" ".join( [(autor.nombre) for autor in autores_queryset])
    contexto = {
        "autores": autores_queryset,
    }
    if request.method =='POST':
        nuevo_autor = {
            "nombre" : request.POST['nombre'],
            "edad": request.POST['edad'],
            "fecha_de_publicacion" : request.POST['fecha_de_publicacion']
        }
        print(request.POST['fecha_de_publicacion'])
        Autor.objects.create(**nuevo_autor)
        autores_queryset = Autor.objects.all()
   
        contexto = {
            "autores": autores_queryset,
            'mensaje' : "El auto fue creado con exito",
        }
        
    return render(request,'autores/autores_lista.html',contexto)


def get_autor(request,pk):
    try:
        autor = Autor.objects.get(pk=pk)
        contexto = {'autor':autor}
        return render(request,'autores/autor_detalle.html',contexto)
    except Exception as e:
        contexto = {'autor': ""}
        return render(request,'autores/autor_detalle.html',contexto)
    

