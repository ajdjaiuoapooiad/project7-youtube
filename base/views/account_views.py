from base.models import User,Item,Profile
from base.forms import UserCreateForm
from django.views import generic
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model


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
    
class ProfileUpdateView(generic.UpdateView):
    model=Profile
    template_name='pages/user_profile.html'
    fields={'name','prefecture','city','address1','address2','tel'}
    success_url='/profile/'

    def get_object(self):
        # URL変数ではなく、現在のユーザーから直接pkを取得
        self.kwargs['pk']=self.request.user.pk
        return super().get_object()   
    
class AccountUpdateView(generic.UpdateView):
    model=get_user_model()
    template_name='pages/user_account.html'
    fields={'username','email'}
    success_url='/account/'
    
    def get_object(self):
        # URL変数ではなく、現在のユーザーから直接pkを取得
        self.kwargs['pk']=self.request.user.pk
        return super().get_object()  