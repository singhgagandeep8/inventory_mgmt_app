from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import loader
from django.shortcuts import render, get_object_or_404,redirect
from django.views import generic
from django.forms import ModelForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
        # creating a dictionary:
        template = loader.get_template('itake/index.html')
        return render(request,'itake/index.html')

#def productList(request):
        #all_product = Product.objects.all()
        #context = {'all_product':all_product}
        #return render(request,'itake/product.html',context)






#use class to create view

#class for product

class productForm(ModelForm):
        class Meta:
                model = Product
                fields = ['productName', 'category', 'description', 'price', 'maxProduct', 'autoRequest',
                  'thresholdLevel', 'quantity', 'productID', 'vendor', 'warehouse']

#view for productList page
class productList(generic.ListView):
        template_name = 'itake/product.html'
        context_object_name = 'all_product'
        def get_queryset(self):
                return Product.objects.all()

#view for productForm page (add products)
class productCreate(CreateView):
        model = Product
        fields = ['productName','category','description','price','maxProduct','autoRequest',
                  'thresholdLevel','quantity','productID','vendor','warehouse']

#update view
def productUpdate(request, product_id, template_name='itake/product_form.html'):
    product=get_object_or_404(Product,pk=product_id)
    form=productForm(request.POST or None, instance=product)
    ctx = {"form": form, "product": product}
    if form.is_valid():
        form.save()
        return redirect('itake:productList')
    return render(request,template_name,ctx)

#view for product detail page
def productDetails(request, product_id):
        product= get_object_or_404(Product,pk=product_id)
        context = {'product': product}
        return render(request, 'itake/productDetails.html', context)

#view for product delete
def productDelete(request, product_id, template_name='itake/productDeleteConfirm.html'):
    product= get_object_or_404(Product, pk=product_id)
    if request.method=='POST':
        product.delete()
        return redirect('itake:productList')
    ctx = {"product": product}
    return render(request, template_name, ctx)


#========================for vendor=======================================

# view for vendorList page
class vendorList(generic.ListView):
        template_name = 'itake/vendor.html'
        context_object_name = 'all_vendor'

        def get_queryset(self):
                return Vendor.objects.all()

#view for vendorDetails page
def vendorDetails(request, vendor_id):
        vendor = get_object_or_404(Vendor,pk=vendor_id)
        product=vendor.vendor.all()
        context = {'vendor': vendor,'product':product}
        return render(request, 'itake/vendorDetails.html', context)

#view for vendorForm page (add products)
class vendorCreate(CreateView):
        model = Vendor
        fields = ['vendorName','vendorPhone']

#===================================for order=================================

class orderList(generic.ListView):
    template_name = 'itake/order.html'
    context_object_name = 'all_order'

    def get_queryset(self):
        return Order.objects.all()

#view for orderDetails page
def orderDetails(request,order_id):
        order = get_object_or_404(Order,pk=order_id)
        orderitem = order.items.all()
        context = {'order': order,'orderitem':orderitem}
        return render(request, 'itake/orderDetails.html', context)

#view for order page

class orderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['orderID', 'products', 'requestedDate', 'receivedDate', 'orderStatus']



class orderCreate(CreateView):
        model = Order
        fields = ['orderID','products','requestedDate','receivedDate','orderStatus']



class orderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order','product','orderQuantity']

#===========================================view for login page===============================

def login1(request):
    if 'register' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name = last_name)
        user.save()
        return render(request, 'itake/Login_page.html')
    elif 'login-form' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            #return render(request, 'login/thankyou.html')
            return render(request, 'itake/index.html')
        else:
            return render(request, 'itake/Login_page.html')
    else:
        return render(request, 'itake/Login_page.html')


