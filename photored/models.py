from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import secrets
# from .paystack import Paystack

class Profile_image(models.Model):
    image = models.ImageField(upload_to='profile_images/')

# class CartItem(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     # Add the following attributes for calculating the total cost
#     price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
#     def calculate_total(self):
#         return self.quantity * self.price
    
#     def __str__(self):
#         return f"{self.user.username}'s Cart Item - {self.product.name}"



# # Create your models here.
# class UserWallet(models.Model):
# 	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
# 	currency = models.CharField(max_length=50, default='GHS')
# 	balance = models.PositiveIntegerField(default=0)
# 	created_at = models.DateTimeField(default=timezone.now, null=True)

# 	def __str__(self):
# 		return self.user.__str__()


# class Payment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
#     amount = models.PositiveIntegerField()
#     ref = models.CharField(max_length=200)
#     email = models.EmailField()
#     verified = models.BooleanField(default=False)
#     date_created = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ('-date_created',)

#     def __str__(self):
#         return f"Payment: {self.amount}"

    # def save(self, *args, **kwargs):
    #     while not self.ref:
    #         ref = secrets.token_urlsafe(50)
    #         object_with_similar_ref = Payment.objects.filter(ref=ref)
    #         if not object_with_similar_ref:
    #             self.ref = ref

    #     super().save(*args, **kwargs)
    
    # def amount_value(self):
    #     return int(self.amount) * 100

    # def verify_payment(self):
    #     paystack = Paystack()
    #     status, result = paystack.verify_payment(self.ref, self.amount)
    #     if status:
    #         if result['amount'] / 100 == self.amount:
    #             self.verified = True
    #         self.save()
    #     if self.verified:
    #         return True
    #     return False
    
# class wishlist(models.Model):
#      user = models.ForeignKey(User, on_delete=models.CASCADE)
#      product = models.ForeignKey(Product, on_delete=models.CASCADE)

#      def __str__(self):
#         return f"{self.user.username}'s Wish list- {self.product.name}"


class UserProfile(models.Model):
    image = models.ImageField()
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    
    def __str__(self):
        return self.user.username
    
#     # models.py
# from django.db import models
# from django.contrib.auth.models import User

# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     ref = models.CharField(max_length=200, default=str(timezone.now))  # Use str(timezone.now) to set a default string value
#     product = models.CharField(max_length=255, default="Product Name")  # Set a default product name
#     amount = models.PositiveIntegerField(default=1)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     first_name = models.CharField(max_length=100, default="")
#     last_name = models.CharField(max_length=100, default="")
#     email = models.EmailField(default="sparkescel@gmail.com")  # Set a default email
#     shipping_address = models.CharField(max_length=255, default="")
#     telephone_number = models.CharField(max_length=20, default="")
#     order_notes = models.TextField(blank=True, default="")
#     create_account = models.BooleanField(default=False)
#     ship_different_address = models.BooleanField(default=False)
#     country = models.CharField(max_length=50, default='unknown')

#     def __str__(self):
#         return f"Order for {self.user.username}"

# from django.contrib.auth.models import AbstractUser, Permission
# from django.db import models

# class CustomUser(AbstractUser):
#     # Your custom fields here
#     profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

#     class Meta:
#         permissions = [
#             ("can_view_custom_content", "Can view custom content"),
#             ("can_edit_profile", "Can edit profile"),
#             # Add more permissions as needed
#         ]
#     user_permissions = models.ManyToManyField(Permission, verbose_name=('user permissions'),
#                                                blank=True, related_name='custom_user_permissions',)