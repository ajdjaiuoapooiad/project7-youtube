from base.models import User,Item
from base.forms import UserCreateForm
from django.views import generic
from django.contrib.auth.views import LoginView


class SignupView(generic.CreateView):
    form_class=UserCreateForm
    template_name='pages/signup_login.html'
    success_url='/login/'
    
class Login(LoginView):
    template_name='pages/signup_login.html'
    
    
class UserListView(generic.ListView):
    template_name='pages/user_list.html'
    model=Item
 
    
class GoodView(generic.ListView):
    template_name='pages/user_good.html'
    model=Item
    
class LikeView(generic.ListView):
    template_name='pages/user_like.html'
    model=Item    
    