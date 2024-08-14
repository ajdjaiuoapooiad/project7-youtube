from django.views import generic
from base.models import Item
from base.forms import ItemCreateForm


class ItemListView(generic.ListView):
    model=Item
    template_name='pages/item_list.html'
    queryset=Item.objects.filter(is_published=True)    
    
class ItemDetailView(generic.DetailView):
    model=Item
    template_name='pages/item_detail.html'

class ItemCreateView(generic.CreateView):
    form_class=ItemCreateForm
    template_name='pages/item_form.html'
    success_url='/'
    
    
    
class ItemUpdateView(generic.UpdateView):
    model=Item
    form_class=ItemCreateForm
    template_name='pages/item_update.html'
    success_url='/'

class ItemDeleteView(generic.DeleteView):
    success_url='/'
    model=Item
    template_name='pages/item_confirm_delete.html'