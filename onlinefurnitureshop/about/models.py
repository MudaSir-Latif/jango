from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    stock = models.IntegerField()
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    waranty = models.CharField(max_length=100,null=True, blank=True, default=None)
    discount = models.CharField(max_length=100,null=True, blank=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.title

class Colour(models.Model):
    colour_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    colour = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.colour


class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')


    def __str__(self):
        return f"Image for {self.product.title}"

class Size(models.Model):
    size_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.size_id


    

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(default=1)  # Assuming default quantity is 1
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart ID: {self.cart_id}, Product: {self.product.title}, Quantity: {self.quantity}"    


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    # ISS PR MAXIMUM 12 DECIMALS KI RESTRICTIONS LAGANI HAI THROUGH FORMS AUR VIEWS
    contact_number =models.IntegerField()

    def __str__(self):
        return f"Supplier ID: {self.supplier_id}, Name: {self.name}, Contact Number: {self.contact_number}"


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    delivery_status = models.CharField(max_length=100)
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order ID: {self.order_id}, Status: {self.delivery_status}, Date: {self.order_date}, Amount: {self.total_amount}"
