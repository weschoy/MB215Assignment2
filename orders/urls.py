from django.conf.urls import url, include
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from orders.views import OrderView

urlpatterns = [
    url(r'^$', OrderView.as_view())
]