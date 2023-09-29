from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home page"),
    path('api-reference/get-basic/',views.api_ref,name="api reference"),
    path('api-reference/get-basic-endpoints/',views.endpoints,name="end points"),
    path('api-reference/transaction-add/',views.transaction_add,name="end points"),
    path('api-reference/transaction-add/',views.transaction_add,name="add transaction"),
    path('api-reference/transaction-endpoints/',views.transaction_endpoint,name="transactions endpoints"),
    path('api-reference/batchs-add/',views.batchs_add,name="batchs add"),
    path('api-reference/batchs-endpoints/',views.batchs_endpoint,name="batchs endpoints"),
    path('auth/',views.auth,name="check authentication"),
    path('transaction-add/',views.auth_transaction_add,name="check authentication")
]