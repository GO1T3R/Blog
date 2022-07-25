from django.shortcuts import render

#para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate



def index(request):
    return render(request, "blogapp/index.html")


def contacto(request):
    return render(request, "blogapp/contacto.html")

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
                usuario = form.cleaned_data.get('username')
                contra = form.cleaned_data.get('password')

                user = authenticate(username=usuario, password=contra)

                if user is not None:
                    login(request, user)
                    
                    return render(request, "blogapp/index.html", {"mensaje":f"Bienvenido {usuario}"})
                else:

                    return render(request, "blogapp/index.html", {"mensaje":"Error, Datos Incorrectos"})
            
        else:

                    return render(request, "blogapp/index.html", {"mensaje":"Error, Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "blogapp/login.html", {'form':form})

def base(request):
    return render(request, "blogapp/base.html")

def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)
        #form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request,"blogapp/iindex.html", {"mensaje":"Usuario creado con exito"})
    
    else:
        form = UserCreationForm()

    
    return render(request, "blogapp/register.html", {"form":form})