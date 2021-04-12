from django.test import TestCase
from sms.models import Order

# Create your tests here.

class OrderListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 10 orders for context test
        number_of_orders=10
        for order_id in range(number_of_orders):
            Order.objects.create(
                phone=f'{order_id}',
                data='{"STATE":"WELCOMING"}',
            )
         

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_view_context_has_orders(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['orders']) == 10)
    def test_view_orders_have_phone(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['orders']) == 10)
        aOrders = response.context['orders']
        for order in aOrders:
            self.assertTrue(order.phone !=None, "has phone number")
        

        