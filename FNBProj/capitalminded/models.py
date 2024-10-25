# your_app/models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,  PermissionsMixin
from django.db import models
 

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email
    
    # class CustomUser(AbstractBaseUser, PermissionsMixin):
    #     email = models.EmailField(unique=True)
    #     is_active = models.BooleanField(default=True)
    #     is_staff = models.BooleanField(default=False)
    #     is_superuser = models.BooleanField(default=False)

    #     USERNAME_FIELD = 'email'
    #     REQUIRED_FIELDS = []

    #     objects = CustomUserManager()

    #     def __str__(self):
    #      return self.email
    
    


class BusinessRegistration(models.Model):
    business_name = models.CharField(max_length=255)
    ownership = models.TextField()
    tax_reg = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    annual_revenue = models.DecimalField(max_digits=10, decimal_places=2)
    product_info = models.TextField()
    business_plan = models.FileField(upload_to='business_plans/')
    financial_statements = models.FileField(upload_to='financial_statements/')
    legal_documents = models.FileField(upload_to='legal_documents/')
    management_profiles = models.FileField(upload_to='management_profiles/')
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_name

# Custom user manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
            
        return self.create_user(email, password, **extra_fields)

# Custom user model
class CustomUser(AbstractBaseUser, PermissionsMixin):  # Inherit PermissionsMixin
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()  # Define the custom manager

    def __str__(self):
        return self.email