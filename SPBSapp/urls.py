from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('custinfo', views.custinfo),
    path('cookie_select', views.cookie_select),
    path('my_story', views.my_story),
    path('gallery', views.gallery),
    path('menu', views.menu), 
    path('faq', views.faq),
    path('contact', views.contact),
    path('birthday', views.birthday),
    path('celebration', views.celebration),
    path('holiday', views.holiday)
]