from django.contrib.auth.mixins import LoginRequiredMixin

class LoginRequidMixinWithLoginURL(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = "redirect_to"