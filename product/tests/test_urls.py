from django.test import SimpleTestCase
from django.urls import reverse, resolve
from product.views import ProductsList, ProductCreate, ProductDelete, purchased_view, UpdateProduct


class TestUrls(SimpleTestCase):

    def test_product_list_url(self):
        url = '/'
        self.assertEquals(resolve(url).func.view_class, ProductsList)

    def test_product_create_list_url(self):
        url = reverse('create')
        self.assertEquals(resolve(url).func.view_class, ProductCreate)

    def test_product_delete_url(self):
        url = reverse('delete_product')
        self.assertEquals(resolve(url).func.view_class, ProductDelete)

    def test_product_purchased_url(self):
        url = reverse('purchased', args=[12])
        self.assertEquals(resolve(url).func, purchased_view)

    def test_product_update_url(self):
        url = reverse('update_product', args=[2])
        self.assertEquals(resolve(url).func.view_class, UpdateProduct)
