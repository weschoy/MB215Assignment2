from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.urls import path, include





urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^simulator/', TemplateView.as_view(template_name="index.html")),
    url(r'^sms/', include('sms.urls')),
    url('', include('orders.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='orderlist.html'), name='home'), 
    path('accounts/', include('accounts.urls')),
    


]