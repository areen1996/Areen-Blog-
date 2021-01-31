from django.urls import path 
#from . import views 
from .views import Homeview , Describtion , Categoryview

urlpatterns = [
   # path('', views.home , name='home'),
   path ('', Homeview.as_view() , name='home' ), 
   path('article/<int:pk>' , Describtion.as_view() , name='describtion'),
   path('category/>' , Categoryview.as_view() , name='category')

]
