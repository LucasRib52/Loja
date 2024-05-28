from stores.models import Store
from stores.forms import ItemModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

    
class StoresListView(ListView):
    model = Store
    template_name = 'stores.html'
    context_object_name = 'stores'

    def get_queryset(self):
        stores = super().get_queryset().order_by('brand')
        search = self.request.GET.get('search')
        if search:
            stores = stores.filter(item__icontains=search)
        return stores
    
class StoreDetailView(DetailView):
    model = Store
    template_name = 'store_detail.html'

@method_decorator(login_required(login_url='login'), name='dispatch')    
class NewItemCreateView(CreateView):
    model = Store
    form_class = ItemModelForm
    template_name = 'new_item.html'
    success_url = '/stores/'


@method_decorator(login_required(login_url='login'), name='dispatch')  
class StoreUpdateView(UpdateView):
    model = Store
    form_class = ItemModelForm
    template_name = 'store_update.html'
    
    def get_success_url(self):
        return reverse_lazy('store_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='login'), name='dispatch')  
class StoreDeleteView(DeleteView):
    model = Store
    template_name = 'store_delete.html'
    success_url = '/stores/'