from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from .forms import UsuarioForm, UnidadForm, RolForm, JerarquiaForm, TareasForm, TareasSubForm
from .models import User, Usuario, Unidad, Rol, Jerarquia, Tarea, TareaSub
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'Quien eres, Que quieres!!!!'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin.html')


def customer(request):
    return render(request,'customer.html')


def employee(request):
    return render(request,'employee.html')

#Comienzo Usuario Admin

def AgregarUsuario(request):
    data = {
        'form': UsuarioForm()       
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    return render(request,'CrudAdmin/agregar.html', data)

def ListarUsuario(request):
    Usuarios = Usuario.objects.all()
    data = {
        'Usuarios': Usuarios
    }
    return render(request, 'CrudAdmin/listar.html', data)

def ModificarUsuario(request, id):
    usuario = get_object_or_404 (Usuario,id=id)
    data = {
        'form': UsuarioForm(instance=usuario)
    }

    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="ListarUsuario")
        data["form"] = formulario

    return render(request, 'CrudAdmin/Modificar.html', data)

def EliminarUsuario(request,id):
    usuario = get_object_or_404(Usuario,id=id)
    usuario.delete()
    return redirect(to="ListarUsuario")

#Fin Tareas Admin

def AgregarUnidad(request):
    data = {
        'form': UnidadForm()
    }
    if request.method == 'POST':
        formulario = UnidadForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    return render(request,'CrudUni/agregar.html', data)

def AgregarRol(request):
    data = {
        'form': RolForm()
    }
    if request.method == 'POST':
        formulario = RolForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    return render(request,'CrudRo/agregar.html', data)

def AgregarJerarquia(request):
    data = {
        'form': JerarquiaForm()
    }
    if request.method == 'POST':
        formulario = JerarquiaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    return render(request,'CrudJer/agregar.html', data)

#Comienzo Tareas Funcionario

def AgregarTarea(request):
    data = {
        'form': TareasForm()
    }
    if request.method == 'POST':
        formulario = TareasForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    return render(request,'TareasFun/agregar.html', data)

def ListarTarea(request):
    Tareas = Tarea.objects.all()
    data = {
        'Tareas': Tareas
    }
    return render(request, 'TareasFun/listar.html', data)


def ModificarTarea(request, id):
    tarea = get_object_or_404 (Tarea,id=id)
    data = {
        'form': TareasForm(instance=tarea)
    }

    if request.method == 'POST':
        formulario = TareasForm(data=request.POST, instance=tarea)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="ListarTarea")
        data["form"] = formulario

    return render(request, 'TareasFun/Modificar.html', data)

def EliminarTarea(request,id):
    tarea = get_object_or_404(Tarea,id=id)
    tarea.delete()
    return redirect(to="ListarTarea")

#Fin Tareas Funcionario

#Comienzo Tareas Subordinadas Funcionario
def AgregarTareaSub(request):
    data = {
        'form': TareasSubForm()
    }
    if request.method == 'POST':
        formulario = TareasSubForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    return render(request,'TareasSub/agregar.html', data)

def ListarTareaSub(request):
    Tareassub = TareaSub.objects.all()
    data = {
        'Tareassub': Tareassub
    }
    return render(request, 'TareasSub/listar.html', data)


def ModificarTareaSub(request, id):
    tareasub = get_object_or_404 (Tareasub,id=id)
    data = {
        'form': TareasSubForm(instance=tareasub)
    }

    if request.method == 'POST':
        formulario = TareasSubForm(data=request.POST, instance=tareasub)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="ListarTarea")
        data["form"] = formulario

    return render(request, 'TareasSub/modificar.html', data)

def EliminarTareaSub(request,id):
    tareasub = get_object_or_404(Tareasub,id=id)
    tareasub.delete()
    return redirect(to="ListarTarea")