from . import views
from django.urls import path
app_name= 'mart'

urlpatterns = [

    path('', views.allprodcat, name='allprodcat'),
    path('<slug:c_slug>/', views.allprodcat, name='products_by_category'),


]
