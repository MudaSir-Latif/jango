from django.db import models

# Create your models here.

# class User(models.Model):
    
#     user_id = models.AutoField(primary_key=True)
#     password = models.CharField(max_length=128)
#     username = models.CharField(max_length=150, unique=True)
#     email = models.EmailField(unique=True)

#     def __str__(self):
#         return self.username

# class Address(models.Model):
#     add_id = models.ForeignKey(User, related_name='addresses', on_delete=models.CASCADE)
#     address = models.CharField(max_length=255)

#     def __str__(self):
#         return self.address

# class PhoneNumber(models.Model):
#     phone_id = models.ForeignKey(User, related_name='phone_numbers', on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=20)

#     def __str__(self):
#         return self.phone_number
