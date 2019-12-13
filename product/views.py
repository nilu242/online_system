from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, View

from allauth.account.decorators import verified_email_required

from product.models import Product, Order


class ProductDetailView(DetailView):
    '''
    product detail class
    '''
    model = Product
    context_object_name = 'product'

class ProductView(ListView):
    '''
    product view list class
    '''
    model = Product
    success_url = '/charge'


    @method_decorator(verified_email_required)
    def dispatch(self, *args, **kwargs):
        return super(ProductView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super(ProductView, self).get_context_data(**kwargs)
        if self.request.user.role == 'admin':
            list_of_product = Product.objects.filter(user=self.request.user)
            context['list_of_product'] = list_of_product

        else:
            list_of_product = Product.objects.all()
            context['list_of_product'] = list_of_product
            context['key'] = settings.STRIPE_PUBLISHABLE_KEY

        return context

class ProductCreate(CreateView):
    '''
    product create class
    '''
    model = Product
    fields = ['product_name', 'description', 'price', 'image']
    success_url = '/'

    @method_decorator(verified_email_required)
    def dispatch(self, *args, **kwargs):
        return super(ProductCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        ''' form '''
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(ProductCreate, self).form_valid(form)

class ProductDelete(View):
    """
    product delete class
    """
    def  get(self, request):
        ''' get data '''
        id = request.GET.get('id', None)
        Product.objects.get(id=id).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

class UpdateProduct(View):
    '''
    product update class
    '''
    def  get(self, request, *args, **kwargs):
        product_id = request.GET.get('id', None)
        name = request.GET.get('name', None)
        description = request.GET.get('description', None)
        price = request.GET.get('price', None)
        form = ProductUpdateForm()
        return render(request, 'product_list.html',{'form',form})

    def post(self, request, *args, **kwargs):
        form = ProductUpdateForm(data=request.POST)
        if form.is_valid():
            
            form = ProductUpdateForm()
            return render(request, 'product_list.html.html', {'form': form})
        return render(request, 'product_list.html.html', {'form': form})

        # data = {
        #     'id' : product.id,
        #     'name' : product.product_name,
        #     'description' : product.description,
        #     'price' : product.price
        # }

        return JsonResponse(data)

def purchased_view(request, pk):
    ''' purchased  '''
    print('ok')
    order = Order()
    order.product = Product.objects.get(id=pk)
    order.user = request.user
    order.price = order.product.price
    order.save()
    return render(request, 'product/charge.html')
