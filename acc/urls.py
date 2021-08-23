from django.urls import path
from . import views
from .views import redirect_view


urlpatterns = [
    path('',views.home,name='home'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('products/',views.products,name='products'),
    path('stock/',views.stock,name='stock'),
    path('main/',views.main,name='main'),
    path('navbar/',views.navbar,name='navbar'),
    path('footer/',views.footer,name='footer'),
    path('sign_in/',views.sign_in,name='sign_in'),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('engineers/',views.sign_in,name='engineers'),
    path('purchases/',views.purchases,name='purchases'),
    path('reports/',views.reports,name='reports'),
    path('requests/',views.requests,name='requests'),
    path('vendors/',views.vendors,name='vendors'),
    path('returns/',views.requests,name='returns'),
    path('accounts/',views.requests,name='accounts'),
    path('about/',views.requests,name='about'),
    path('services/',views.requests,name='services'),

  
   

   

]