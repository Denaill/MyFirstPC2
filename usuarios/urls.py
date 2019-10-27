from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
   url(r'^registrar', views.RegistroUsuario.as_view(), name="registrar"),
]