# your_app/models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,  PermissionsMixin
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


    
class BusinessRegistration(models.Model):
    business_name = models.CharField(max_length=255)
    ownership = models.CharField(max_length=255)
    tax_reg = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    annual_revenue = models.DecimalField(max_digits=10, decimal_places=2)
    product_info = models.TextField()
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    business_plan = models.FileField(upload_to='business_plans/', null=True, blank=True)
    financial_statements = models.FileField(upload_to='financial_statements/', null=True, blank=True)
    legal_documents = models.FileField(upload_to='legal_documents/', null=True, blank=True)
    management_profiles = models.FileField(upload_to='management_profiles/', null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_name


# class BusinessRegistration(models.Model):
#     business_name = models.CharField(max_length=255)
#     ownership = models.TextField()
#     tax_reg = models.CharField(max_length=100)
#     industry = models.CharField(max_length=100)
#     annual_revenue = models.DecimalField(max_digits=10, decimal_places=2)
#     product_info = models.TextField()
#     business_plan = models.FileField(upload_to='business_plans/')
#     financial_statements = models.FileField(upload_to='financial_statements/')
#     legal_documents = models.FileField(upload_to='legal_documents/')
#     management_profiles = models.FileField(upload_to='management_profiles/')
#     logo = models.ImageField(upload_to='logos/', blank=True, null=True)
#     submitted_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.business_name

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


class BusinessType(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class BusinessResource(models.Model):
    business_type = models.ForeignKey(BusinessType, related_name='resources', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class MicroLoan(models.Model):
    LOAN_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('ACTIVE', 'Active'),
        ('PAID', 'Paid'),
    ]

    business = models.ForeignKey('BusinessRegistration', on_delete=models.CASCADE)
    amount_requested = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    term_months = models.IntegerField()
    purpose = models.TextField()
    status = models.CharField(max_length=20, choices=LOAN_STATUS_CHOICES, default='PENDING')
    application_date = models.DateTimeField(auto_now_add=True)
    approval_date = models.DateTimeField(null=True, blank=True)
    monthly_payment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def calculate_monthly_payment(self):
        # Convert all numbers to Decimal for consistent calculation
        r = Decimal(str(self.interest_rate)) / Decimal('100') / Decimal('12')  # Monthly interest rate
        n = Decimal(str(self.term_months))  # Convert term_months to Decimal
        p = Decimal(str(self.amount_requested))
        
        # Calculate (1 + r)^n
        power_term = (Decimal('1') + r) ** n
        
        # Calculate monthly payment
        monthly_payment = p * (r * power_term) / (power_term - Decimal('1'))
        
        # Round to 2 decimal places
        return round(monthly_payment, 2)

    def save(self, *args, **kwargs):
        if not self.monthly_payment:
            self.monthly_payment = self.calculate_monthly_payment()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Loan for {self.business.business_name} - ${self.amount_requested}"