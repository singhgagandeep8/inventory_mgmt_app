from django.db import models
from datetime import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib import admin

# Create your models here.


class Vendor(models.Model):
    vendorName = models.CharField(max_length=500)
    vendorPhone = models.CharField(max_length=500, null=True)
    vendorEmail = models.CharField(max_length=500, null=True)
    vendorID = models.CharField(max_length=100,blank=True, null=True)
    def __str__(self):
        return self.vendorName
# when the new product is added, it should be displayed in the detail /list pate?
    def get_absolute_url(self):
        return reverse('itake:vendorList')



class Warehouse(models.Model):
    warehouseID = models.IntegerField(primary_key=True)
    warehouseName = models.CharField(max_length=100,blank=True, null=True)
    warehouseAddress = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.warehouseName



class Product(models.Model):
    productName =  models.CharField(max_length=500)
    category = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    maxProduct = models.IntegerField(default=30)
    autoRequest = models.BooleanField()
    thresholdLevel = models.IntegerField(default=30)
    quantity = models.IntegerField(default=20)
    productID = models.CharField(max_length=100, blank=True, null=True)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True,related_name='vendor')
    warehouse = models.ManyToManyField(Warehouse,related_name="pro_ware", through="ProductWarehouse")
    def __str__(self):
        return self.productName + "-" + self.category
#when the new product is added, it should be displayed in the detail /list pate?
    def get_absolute_url(self):
        return reverse('itake:productList')

class ProductWarehouse(models.Model):
    warehouse=models.ForeignKey(Warehouse,on_delete=models.CASCADE,null=True, related_name='warehouse')
    product=models.ForeignKey(Product, on_delete=models.CASCADE,null=True, related_name='warepro')
    quantity = models.IntegerField(default=20)
    def __str__(self):
        return self.product.productName + '-' +self.warehouse.warehouseName


class Order(models.Model):
    orderID = models.CharField(max_length=100, blank=True, null=True)
    products = models.ManyToManyField(Product,related_name="order_item", through="OrderItem")
    requestedDate = models.DateField(default=datetime.now, blank=True, null=True)
    receivedDate = models.DateField(default=datetime.now, blank=True, null=True)
    orderStatus = models.CharField(max_length=100,blank=True, null=True)
    #sumPrice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #receivedDate = models.CharField(max_length=100,blank=True, null=True)


    def __str__(self):
        return self.orderID


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True, related_name='product')
    #cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE, null=True,related_name='items')
    orderQuantity = models.IntegerField(default=10)
    #orderItemID = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.order.orderID + '-' +self.product.productName




#admin models
class OrderAdmin(admin.ModelAdmin):
    class OrderItemInline(admin.TabularInline):
        model = OrderItem
    inlines = [OrderItemInline,]

class ProWareAdmin(admin.ModelAdmin):
    class ProWareInline(admin.TabularInline):
        model = ProductWarehouse
    inlines = [ProWareInline,]