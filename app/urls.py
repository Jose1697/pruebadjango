from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^product$', views.ProductList.as_view()),
    url(r'product/(?P<pk>[0-9]+)$', views.ProductDetail.as_view()),

]

