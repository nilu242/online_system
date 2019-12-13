from django.db import models


class Product(models.Model):
    """
    Model for product.
    """

    user = models.ForeignKey('core.User', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product_images', blank=True)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    """
    Model for product history.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey('core.User', on_delete=models.CASCADE)
    buying_date = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField()
