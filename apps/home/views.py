from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Home
from django.contrib import messages
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator
from .forms import UserForm, PersonaForm
from apps.persona.models import Persona
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from common.mixins import LoginRequidMixinWithLoginURL


@method_decorator(xframe_options_exempt, name="dispatch")
class HomeView(TemplateView):
    name = "home"
    template_name = "home.html"

    # render name in template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        home_instance, created = Home.objects.get_or_create(
            id=1,
            defaults={
                "banner": "home/example.jpg",
                "botonMenu": "home/example.jpg",
                "botonReservation": "home/example.jpg",
                "botonSeguimientoDePedido": "home/example.jpg",
            },
        )
        if home_instance:
            context["banner"] = home_instance.banner
            context["botonmenu"] = home_instance.botonMenu
            context["botonreservacion"] = home_instance.botonReservation
            context["botonseguimientodepedido"] = home_instance.botonSeguimientoDePedido
        return context


@method_decorator(xframe_options_exempt, name="dispatch")
class HomeEditView(LoginRequidMixinWithLoginURL, TemplateView):
    name = "edit_home"
    template_name = "home_edit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        home = Home.objects.first()
        if home:
            context["banner"] = home.banner
            context["botonmenu"] = home.botonMenu
            context["botonreservacion"] = home.botonReservation
            context["botonseguimientodepedido"] = home.botonSeguimientoDePedido

        return context

    def post(self, request, *args, **kwargs):
        home = Home.objects.first()
        if not home:
            home = Home.objects.create()

        # Actualizar usando los nombres correctos del modelo
        home.banner = request.FILES.get("banner")
        home.botonMenu = request.FILES.get("botonmenu")  # Notar la M mayúscula
        home.botonReservation = request.FILES.get("botonreservacion")  # Notar la R mayúscula
        home.botonSeguimientoDePedido = request.FILES.get("botonseguimientodepedido")  # Notar las mayúsculas

        home.save()
        messages.success(request, "Contenido actualizado exitosamente")
        return self.render_to_response(self.get_context_data(**kwargs))


class HomeAbout(TemplateView):
    name = "about"
    template_name = "about.html"

    # render name in template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        home_instance, created = Home.objects.get_or_create(
            id=1,
            defaults={
                "banner": "home/example.jpg",
                "botonMenu": "home/example.jpg",
                "botonReservation": "home/example.jpg",
                "botonSeguimientoDePedido": "home/example.jpg",
            },
        )
        if home_instance:
            context["banner"] = home_instance.banner
            context["botonmenu"] = home_instance.botonMenu
            context["botonreservacion"] = home_instance.botonReservation
            context["botonseguimientodepedido"] = home_instance.botonSeguimientoDePedido
        return context


@method_decorator(xframe_options_exempt, name="dispatch")
class LoginView(TemplateView):
    name = "login"
    template_name = "login.html"
    login_url = "/login/"
    redirect_field_name = "redirect_to"

    def post(self, request, *args, **kwargs):
        # Obtiene el username y password del formulario
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Autentica el usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect_to = request.GET.get(self.redirect_field_name, "home")
            return redirect(redirect_to)  # redirige a la página que se intentó acceder
        else:
            messages.error(
                request, "Credenciales incorrectas"
            )  # Muestra un mensaje de error

        # Si la autenticación falla, recarga el mismo formulario de login
        return render(request, self.template_name)


@method_decorator(xframe_options_exempt, name="dispatch")
class UserCreateForm(LoginRequidMixinWithLoginURL, FormView):
    name = "user_create"
    template_name = "user_create.html"
    success_url = reverse_lazy("home")  # Redirigir al home después de crear el usuario
    form_class = UserForm  # El formulario principal

    def get_context_data(self, **kwargs):
        """Agrega el formulario de Persona al contexto."""
        context = super().get_context_data(**kwargs)
        if "persona_form" not in context:
            context["persona_form"] = PersonaForm()
        return context

    def form_valid(self, form):
        """Procesa los datos del formulario UserForm."""
        persona_form = PersonaForm(self.request.POST)
        if persona_form.is_valid():
            # Guarda el usuario
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])  # Encripta la contraseña
            user.save()

            # Guarda la Persona asociada
            persona = persona_form.save(commit=False)
            persona.user = user
            persona.save()

            messages.success(self.request, "Usuario creado con éxito.")
            return super().form_valid(form)
        else:
            messages.error(self.request, "Error en el formulario de Persona.")
            return self.form_invalid(form)

    def form_invalid(self, form):
        """Manejo de errores del formulario UserForm."""
        messages.error(self.request, "Error en el formulario.")
        return self.render_to_response(self.get_context_data(form=form))


def logout_view(request):
    logout(request)  # Finaliza la sesión del usuario
    return redirect("login")  # Redirige a la página de login
