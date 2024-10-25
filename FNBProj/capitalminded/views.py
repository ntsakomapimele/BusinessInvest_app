from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from . import models
from decimal import Decimal, InvalidOperation

from decimal import Decimal
def login_view(request):
    print("logged in")
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to home page after login
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

def dashboard_view(request): 
    return render(request, 'dashboard.html')

# def business__view(request): 
#     return render(request, 'BusinessReg.html')



# def register_business(request):
#     if request.method == 'POST':
#         print("Passed here +++++++++++++++++++++++++")
        
#         # Retrieve form data
#         business_name = request.POST.get('business_name')
#         ownership = request.POST.get('ownership')
#         tax_reg = request.POST.get('tax_reg')
#         industry = request.POST.get('industry')
#         annual_revenue = request.POST.get('annual_revenue')
#         product_info = request.POST.get('product_info')
#         logo = request.FILES.get('logo')

#         # Handle file uploads
#         business_plan = request.FILES.get('business_plan')
#         financial_statements = request.FILES.get('financial_statements')
#         legal_documents = request.FILES.get('legal_documents')
#         management_profiles = request.FILES.get('management_profiles')

#         # Create and save a new BusinessRegistration instance
#         registration = models.BusinessRegistration(
#             business_name=business_name,
#             ownership=ownership,
#             tax_reg=tax_reg,
#             industry=industry,
#             annual_revenue=annual_revenue,
#             product_info=product_info,
#             business_plan=business_plan,
#             financial_statements=financial_statements,
#             legal_documents=legal_documents,
#             management_profiles=management_profiles,
#             logo=logo,  # Set logo here
#         )
#         registration.save()  # Save the registration to the database

#         # Direct response after successful registration
#         return HttpResponse("Business registration successful.")

#     # If GET request, just render the registration form
#     return render(request, 'BusinessREG.html')

def register_business(request):
    if request.method == 'POST':
        print("Passed here +++++++++++++++++++++++++")
        
        # Retrieve form data
        business_name = request.POST.get('business_name')
        ownership = request.POST.get('ownership')
        tax_reg = request.POST.get('tax_reg')
        industry = request.POST.get('industry')
        annual_revenue = request.POST.get('annual_revenue')
        product_info = request.POST.get('product_info')
        logo = request.FILES.get('logo')

        # Handle file uploads
        business_plan = request.FILES.get('business_plan')
        financial_statements = request.FILES.get('financial_statements')
        legal_documents = request.FILES.get('legal_documents')
        management_profiles = request.FILES.get('management_profiles')

        try:
            # Ensure annual_revenue is valid and convert it to Decimal
            annual_revenue = Decimal(annual_revenue)  # This will raise an exception if invalid

            # Create and save a new BusinessRegistration instance
            registration = models.BusinessRegistration(
                business_name=business_name,
                ownership=ownership,
                tax_reg=tax_reg,
                industry=industry,
                annual_revenue=annual_revenue,
                product_info=product_info,
                business_plan=business_plan,
                financial_statements=financial_statements,
                legal_documents=legal_documents,
                management_profiles=management_profiles,
                logo=logo,  # Set logo here
            )
            registration.save()  # Save the registration to the database

            # Direct response after successful registration
            return HttpResponse("Business registration successful.")

        except (ValueError, InvalidOperation):
            # Handle invalid decimal value
            return HttpResponse("Invalid value for annual revenue. Please enter a valid number.")

    # If GET request, just render the registration form
    return render(request, 'BusinessREG.html')

def view_registrations(request):
    registrations = models.BusinessRegistration.objects.all()
    return render(request, 'view_registrations.html', {'registrations': registrations})

from django.shortcuts import render
from .models import BusinessRegistration

def business_overview(request, business_id):
    # Replace 'business_id' with the actual identifier you're using
    company = get_object_or_404(BusinessRegistration, id=business_id)
    return render(request, 'business_page.html', {'company': company})