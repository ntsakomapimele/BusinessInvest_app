from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from . import models
from decimal import Decimal, InvalidOperation
from django.http import JsonResponse
from .models import BusinessType, BusinessResource
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MicroLoan
from .forms import MicroLoanApplicationForm
from datetime import datetime

@login_required
def apply_for_loan(request, business_id):
    business = get_object_or_404(BusinessRegistration, id=business_id)
    
    if request.method == 'POST':
        form = MicroLoanApplicationForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.business = business
            
            # Set interest rate based on business criteria
            annual_revenue = business.annual_revenue
            if annual_revenue < 50000:
                loan.interest_rate = 12.5
            elif annual_revenue < 100000:
                loan.interest_rate = 10.0
            else:
                loan.interest_rate = 8.5
                
            loan.save()
            messages.success(request, 'Loan application submitted successfully!')
            return redirect('loan_status', loan_id=loan.id)
    else:
        form = MicroLoanApplicationForm()
    
    return render(request, 'loan_application.html', {
        'form': form,
        'business': business
    })

@login_required
def loan_status(request, loan_id):
    loan = get_object_or_404(MicroLoan, id=loan_id)
    return render(request, 'loan_status.html', {'loan': loan})

@login_required
def my_loans(request, business_id):
    business = get_object_or_404(BusinessRegistration, id=business_id)
    loans = MicroLoan.objects.filter(business=business)
    return render(request, 'my_loans.html', {'loans': loans, 'business': business})


def business_type_list(request):
    business_types = BusinessType.objects.all()
    return render(request, 'business_selector.html', {'business_types': business_types})

def get_business_resources(request):
    business_type = request.GET.get('business_type')
    if not business_type:
        return JsonResponse({'error': 'Business type is required'}, status=400)
    
    try:
        resources = BusinessResource.objects.filter(business_type__slug=business_type).values(
            'title', 'url', 'description'
        )
        return JsonResponse({'resources': list(resources)})
    except BusinessType.DoesNotExist:
        return JsonResponse({'error': 'Business type not found'}, status=404)


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
                logo=logo,
            )
            registration.save()

            # Redirect to the business overview page using the new registration's ID
            return redirect(reverse('investment_overview', kwargs={'business_id': registration.id}))

        except (ValueError, InvalidOperation):
            # Handle invalid decimal value
            return HttpResponse("Invalid value for annual revenue. Please enter a valid number.")

    # If GET request, just render the registration form
    return render(request, 'BusinessReg.html')

def view_registrations(request):
    registrations = models.BusinessRegistration.objects.all()
    return render(request, 'view_registrations.html', {'registrations': registrations})

from django.shortcuts import render
from .models import BusinessRegistration

def business_overview(request, business_id):
    # Replace 'business_id' with the actual identifier you're using
    company = get_object_or_404(BusinessRegistration, id=business_id)
    return render(request, 'business_page.html', {'company': company})