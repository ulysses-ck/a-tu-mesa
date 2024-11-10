from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Home
from django.contrib import messages
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator

@method_decorator(xframe_options_exempt, name='dispatch')
class HomeView(TemplateView):
	name = 'home'
	template_name = 'home.html'

	# render name in template
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		home_instance, created = Home.objects.get_or_create(
            id= 1,
            defaults={
                "banner": "https://i.ibb.co/wWdxVVs/ilustracion-delicioso-shoyu-ramen-vista-arriba-fondo-blanco-435599-30529.jpg",
                "botonMenu":"https://cdn.pixabay.com/photo/2017/11/07/07/06/menu-2925825_1280.png",
                "botonReservation":"https://w7.pngwing.com/pngs/629/948/png-transparent-red-round-book-now-button-book-now-buttons-thumbnail.png",
                "botonSeguimientoDePedido":"https://as2.ftcdn.net/v2/jpg/00/16/27/39/1000_F_16273947_3TlCeyAVBlJuphSPEDmllmLUeyAAQezK.jpg"
            }
        )
		if home_instance:
			context['banner'] = home_instance.banner
			context['botonmenu'] = home_instance.botonMenu
			context['botonreservacion'] = home_instance.botonReservation
			context['botonseguimientodepedido'] = home_instance.botonSeguimientoDePedido
		return context

@method_decorator(xframe_options_exempt, name='dispatch')
class HomeEditView(TemplateView):
    name = 'edit_home'
    template_name = 'home_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        home = Home.objects.first()
        if home:
            context['banner'] = home.banner
            context['botonmenu'] = home.botonMenu
            context['botonreservacion'] = home.botonReservation
            context['botonseguimientodepedido'] = home.botonSeguimientoDePedido
            self.template_name = f'{kwargs.get("template_name")}.html'

        return context

    def post(self, request, *args, **kwargs):
        home = Home.objects.first()
        if not home:
            home = Home.objects.create()

        # Actualizar usando los nombres correctos del modelo
        home.banner = request.POST.get('banner', '')
        home.botonMenu = request.POST.get('botonmenu', '')  # Notar la M mayúscula
        home.botonReservation = request.POST.get('botonreservacion', '')  # Notar la R mayúscula
        home.botonSeguimientoDePedido = request.POST.get('botonseguimientodepedido', '')  # Notar las mayúsculas
        
        home.save()
        messages.success(request, 'Contenido actualizado exitosamente')
        return self.render_to_response(self.get_context_data(**kwargs))

class HomeAbout(TemplateView):
	name = 'about'
	template_name = 'about.html'

	# render name in template
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		home_instance, created = Home.objects.get_or_create(
            id= 1,
            defaults={
                "banner": "https://i.ibb.co/wWdxVVs/ilustracion-delicioso-shoyu-ramen-vista-arriba-fondo-blanco-435599-30529.jpg",
                "botonMenu":"https://cdn.pixabay.com/photo/2017/11/07/07/06/menu-2925825_1280.png",
                "botonReservation":"https://w7.pngwing.com/pngs/629/948/png-transparent-red-round-book-now-button-book-now-buttons-thumbnail.png",
                "botonSeguimientoDePedido":"https://as2.ftcdn.net/v2/jpg/00/16/27/39/1000_F_16273947_3TlCeyAVBlJuphSPEDmllmLUeyAAQezK.jpg"
            }
        )
		if home_instance:
			context['banner'] = home_instance.banner
			context['botonmenu'] = home_instance.botonMenu
			context['botonreservacion'] = home_instance.botonReservation
			context['botonseguimientodepedido'] = home_instance.botonSeguimientoDePedido
		return context