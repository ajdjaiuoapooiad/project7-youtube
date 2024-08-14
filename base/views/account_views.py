from base.models import User
from base.forms import AccountCreateForm
from django.views import generic


class SignupView(generic.CreateView):
    form_class=AccountCreateForm
    template_name='pages/signup_login.html'
    success_url='pages/signup_login.html'