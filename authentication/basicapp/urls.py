from django.conf.urls import url
from django.urls import path
from basicapp import views

app_name = 'basicapp'

urlpatterns = [
    path('register/',views.register,name="register"),
    path('userlogin/',views.userlogin,name="userlogin")
]
