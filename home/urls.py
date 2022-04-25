from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('detail/<slug>', ProductDetailView.as_view(), name= 'detail'),
    path('category/<slug>', CategoryView.as_view(), name= 'category'),
    path('subcategory/<slug>', SubCategoryView.as_view(), name= 'subcategory')
]