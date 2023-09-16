from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from django.db import models

class User(AbstractUser):
    roles = (
        ('investor', 'Investor'),
        ('contributor', 'Contributor'),
    )
    role = models.CharField(max_length=20, choices=roles, default='investor')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    address = models.ForeignKey('Address', on_delete=models.CASCADE, null=True, blank=True)
    payment = models.ForeignKey('Payment', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username
    
class Address(models.Model):
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return self.street_address + ', ' + self.city + ', ' + self.state_province + ', ' + self.country + ', ' + self.postal_code
    
class Payment(models.Model):
    payment_methods = (
        ('credit', 'Credit'),
        ('debit', 'Debit'),
        ('paypal', 'PayPal'),
        ('bitcoin', 'Bitcoin'),
    )
    payment_method = models.CharField(max_length=20, choices=payment_methods, default='credit')
    card_number = models.CharField(max_length=20)
    expiration_date = models.DateField()
    security_code = models.CharField(max_length=4)
    billing_address = models.ForeignKey('Address', on_delete=models.CASCADE)

    def __str__(self):
        return self.payment_method + ', ' + self.card_number + ', ' + str(self.expiration_date) + ', ' + self.security_code + ', ' + str(self.billing_address)