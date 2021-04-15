from django.test import TestCase
from sms.models import Order
from django.contrib.auth.models import User
from django.test import Client
import datetime

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


class chronologicalOrderTest(TestCase):
    def test_view_orders_in_order(self):
        response = self.client.get('/')
        login=self.client.login(username='testuser',password='testpassword')
        self.assertEqual(str(response.context['user']), 'AnonymousUser')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('orders' in response.context)
    def order1(self):
        earliest_order=datetime.datetime.now().strftime('%H:%M:%S') 
    def order2(self):
        latest_order=datetime.datetime().strftime('%H:%M:%S') 
    def order1BeforeOrder2(self):
        for meal in response.context['orders']:
            self.assertTrue(order1()<order2())
            
class LoginTest(TestCase):
    def test_login(self):
        c=Client()
        response=c.post('/accounts/login/',{'username':'john','password':'smith'})
        self.assertEqual(response.status_code, 200)
        response=c.get('/')
        response.content

    
        


        

    
    



