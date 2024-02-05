from django.urls import path
from .views import *

urlpatterns = [
    path('pay/',PaymentView.as_view(),name='payment-view'),
    path('products/',ProductsView),
    path('success/',SuccessView),
    path('create/',CreateView),
    path('fail/',FailView),
]