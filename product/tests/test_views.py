from django.test import TestCase, Client
from django.urls import reverse
from product.models import Product, Order
from core.models import User

class TestViews(TestCase):

    def setUp(self):

        self.client = Client()
        self.user = User.objects.create_user('nahar@gmail.com', 'nilesh@123')


        self.list_url = '/'
        self.create_url  = reverse('create')
        self.delete_url = reverse('delete_product')
        self.purchased_url = reverse('purchased',args=[1])


    def test_homepage(self):
        self.client.login(email='nahar@gmail.com', password='nilesh@123')
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)


    def test_create(self):
        self.client.login(email='nahar@gmail.com', password='nilesh@123')
        post = Product.objects.create(user=self.user, product_name="xyz", description="xyz is nice", price='1500',image='xyz.jpeg')
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)

    # def test_purchased(self):
    #     self.client.login(email='nahar@gmail.com', password='nilesh@123')
    #     response = self.client.get(self.purchased_url)
    #     self.assertEqual(response.status_code, 200)
