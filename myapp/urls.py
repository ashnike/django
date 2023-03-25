from django.urls import path
from . import views
urlpatterns = [
    path('',views.myfunctioncall,name="index"),
    path('firstpage',views.firstpage, name='firstpage'),
     path('secpage',views.secpage, name='secpage')
]