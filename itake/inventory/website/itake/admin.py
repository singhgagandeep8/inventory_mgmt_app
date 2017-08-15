from django.contrib import admin
from .models import *
from django.core.urlresolvers import reverse
# Register your models here.

#class OrderAdmin(admin.ModelAdmin):
    #class OrderItemInline(admin.TabularInline):
        #model = OrderItem
    #inlines = [OrderItemInline,]





admin.site.register(Product,ProWareAdmin)
admin.site.register(Vendor)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Warehouse)

