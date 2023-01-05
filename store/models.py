from django.db import models


class Collection(models.Model):
    title = models.CharField(max_length=255)


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DecimalField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)


class Customer(models.Model):
    MEMBERSHIP_STATUS_BRONZE = 'B'
    MEMBERSHIP_STATUS_SILVER = 'S'
    MEMBERSHIP_STATUS_GOLD = 'G'

    MEMBERSHIP_STATUS_CHOICE = [
        (MEMBERSHIP_STATUS_BRONZE, 'Bronze'),
        (MEMBERSHIP_STATUS_SILVER, 'Silver'),
        (MEMBERSHIP_STATUS_GOLD, 'Gold')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=250)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_STATUS_CHOICE, default=MEMBERSHIP_STATUS_BRONZE)


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICE = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICE, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT())
    product = models.ForeignKey(Product, on_delete=models.PROTECT())
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField( max_digits=6, decimal_places=2)