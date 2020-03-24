from django.urls import path
from . import views

app_name ='stocks'
urlpatterns = [

    path('', views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('add_currency.html', views.add_currency, name='add_currency'),
    path('del_currency/<cur_id>', views.del_currency, name='del_currency')
   
]
