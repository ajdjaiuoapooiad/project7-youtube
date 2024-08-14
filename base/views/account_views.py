from base.models import User
from base.forms import AccountCreateForm
from django.views import generic
from django.contrib.auth.views import LoginView


class SignupView(generic.CreateView):
    form_class=AccountCreateForm
    template_name='pages/signup_login.html'
    success_url='/login/'
    
class Login(LoginView):
    template_name='pages/signup_login.html'
    