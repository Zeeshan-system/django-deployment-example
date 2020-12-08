from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('form_page/',views.form_name_view, name='feedback'),
    path('formpage/thankyou',views.thankyou, name='thankyou'),
    path('users',views.users, name='users'),
    path('index',views.index, name='index')
]
