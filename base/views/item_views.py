from django.views import generic
from base.models import Item
from base.forms import ItemCreateForm
from  django.shortcuts import  render,redirect


class ItemListView(generic.ListView):
    model=Item
    template_name='pages/item_list.html'
    queryset=Item.objects.filter(is_published=True)    
    
def detailfunc(request,pk):
    object=Item.objects.get(pk=pk)
    object.read_count += 1 #閲覧数をインクリメント
    object.save()
    return render(request,'pages/item_detail.html',{'object':object})

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
    
    
def goodfunc(request,pk):
    item=Item.objects.get(pk=pk)
    item2=request.user.get_username()
    if item2 in item.usertext:
        return redirect('/')
    else:
        item.good_count += 1
        item.usertext=item.usertext + ' ' + item2
        item.save()
        return redirect('/')