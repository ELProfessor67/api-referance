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
    path('api-reference/customer/',views.customer,name="customer"),
    path('api-reference/create-customer/',views.create_customer,name="create customer"),
    path('auth/',views.auth,name="check authentication"),
    path('transaction-add/',views.auth_transaction_add,name="check authentication"),
    path('batch-add/',views.auth_batch_add,name="batch add"),
    path('api-reference/refunds/',views.refunds,name="refunds"),
    path('api-reference/statement/',views.statement,name="statement"),
    path('api-reference/merchants/',views.merchants,name="merchants"),
    path('api-reference/account/',views.account,name="account"),
    path('api-reference/account-balance/',views.accountbalance,name="accountbalance"),
    path('api-reference/account-bank/',views.accountbank,name="accountbank"),
    path('api-reference/transactiontype/',views.transactiontype,name="transactiontype"),
    path('api-reference/processingcodes/',views.processingcodes,name="processingcodes"),
    path('api-reference/exchangerate/',views.exchangerate,name="exchangerate"),
    path('api-reference/feemodels/',views.feemodels,name="feemodels"),
]