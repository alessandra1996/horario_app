from django.shortcuts import render
from .forms import regform
from .models import registrado

# Create your views here.
def inicio(request):
    form = regform(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        form_data=form.cleaned_data
        er=form_data.get("codigo")
        wer=form_data.get("nombre")
        obj2= registrado.objects.create(codigo=er,nombre=wer)
       
        
        
    return render(request,"inicio.html",context)
