from django.views import generic
from base.models import Item


class ItemListView(generic.ListView):
    model=Item
    template_name='pages/item_list.html'
    queryset=Item.objects.filter(is_published=True)    
    
class ItemDetailView(generic.DetailView):
    model=Item
    template_name='pages/item_detail.html'
 