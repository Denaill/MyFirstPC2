from django.shortcuts import render
from django.views.generic import CreateView
from usuarios.forms import RegistroForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class RegistroUsuario(CreateView):
    model = User
    template_name = "usuarios/usuario_form.html"
    form_class = RegistroForm
    success_url = reverse_lazy('shop:product_list')