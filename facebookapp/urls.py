from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Home,name=''),
    path('syber',views.Link,name='home'),


]