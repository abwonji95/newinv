from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(Order)
admin.site.register(Purchases)
admin.site.register(Product)
admin.site.register(Services)
admin.site.register(Engineers)
admin.site.register(Deployment)


