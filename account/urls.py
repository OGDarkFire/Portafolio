from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('employee/', views.employee, name='employee'),
    path('AgregarUsuario/', views.AgregarUsuario, name='AgregarUsuario'),
    path('ModificarUsuario/<id>/', views.ModificarUsuario, name='ModificarUsuario'),
    path('ListarUsuario/', views.ListarUsuario, name='ListarUsuario'),
    path('EliminarUsuario/<id>/', views.EliminarUsuario, name='EliminarUsuario'),
    path('AgregarUnidad/', views.AgregarUnidad, name='AgregarUnidad'),
    path('AgregarRol/', views.AgregarRol, name='AgregarRol'),
    path('AgregarJerarquia/', views.AgregarJerarquia, name='AgregarJerarquia'),
    path('AgregarTarea/', views.AgregarTarea, name='AgregarTarea'),
    path('ModificarTarea/<id>/', views.ModificarTarea, name='ModificarTarea'),
    path('ListarTarea/', views.ListarTarea, name='ListarTarea'),
    path('EliminarTarea/<id>/', views.EliminarTarea, name='EliminarTarea'),
    path('AgregarTareaSub/', views.AgregarTareaSub, name='AgregarTareaSub'),
    path('ModificarTareaSub/<id>/', views.ModificarTareaSub, name='ModificarTareaSub'),
    path('ListarTareaSub/', views.ListarTareaSub, name='ListarTareaSub'),
    path('EliminarTareaSub/<id>/', views.EliminarTareaSub, name='EliminarTareaSub'),
]