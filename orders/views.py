from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

from sms.models import Order


class OrderView(TemplateView):
    template_name = "orderlist.html"
    def getContext(self, request, *args, **kwargs):
        context = dict()
        context['orders'] = Order.objects.all()
        return context
    def get(self, request, *args, **kwargs):
        context = self.getContext(request, *args, **kwargs)
        return self.render_to_response(context)
    def post(self, request, *args, **kwargs):
        oPost = request.POST.copy()
        oOrder = Order.objects.get(id = oPost['delete'])
        oOrder.delete()
        context = self.getContext(request, *args, **kwargs)
        return self.render_to_response(context)

