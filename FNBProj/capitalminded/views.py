from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from . import models
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
#         # Retrieve form data
#         business_name = request.POST.get('business_name')
#         ownership = request.POST.get('ownership')
#         tax_reg = request.POST.get('tax_reg')
#         industry = request.POST.get('industry')
#         annual_revenue = request.POST.get('annual_revenue')
#         product_info = request.POST.get('product_info')

#         # Handle file uploads
#         business_plan = request.FILES.get('business_plan')
#         financial_statements = request.FILES.get('financial_statements')
#         legal_documents = request.FILES.get('legal_documents')
#         management_profiles = request.FILES.get('management_profiles')

#         # Save files to the file system or a model (if you have one)
#         fs = FileSystemStorage()
#         if business_plan:
#             fs.save(business_plan.name, business_plan)
#         if financial_statements:
#             fs.save(financial_statements.name, financial_statements)
#         if legal_documents:
#             fs.save(legal_documents.name, legal_documents)
#         if management_profiles:
#             fs.save(management_profiles.name, management_profiles)

#         # Redirect or render a success page
#         return HttpResponse("Business registration successful.")

#     return render(request, 'businessReg.html')


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

    # If GET request, just render the registration form
    return render(request, 'BusinessREG.html')



# def register_business(request):
#     print(f"Request method: {request.method}")
    
#     if request.method == 'POST':
#         # Check if POST data and FILES are coming through
#         print(f"POST data: {request.POST}")
#         print(f"FILES data: {request.FILES}")
        
#         # Retrieve form data
#         business_name = request.POST.get('business_name')
#         ownership = request.POST.get('ownership')
#         tax_reg = request.POST.get('tax_reg')
#         industry = request.POST.get('industry')
#         annual_revenue = request.POST.get('annual_revenue')
#         product_info = request.POST.get('product_info')

#         # Handle file uploads
#         business_plan = request.FILES.get('business_plan')
#         financial_statements = request.FILES.get('financial_statements')
#         legal_documents = request.FILES.get('legal_documents')
#         management_profiles = request.FILES.get('management_profiles')

#         # Debugging: print out each field to see the values
#         print(f"Business name: {business_name}")
#         print(f"Ownership: {ownership}")
#         print(f"Tax reg: {tax_reg}")
#         print(f"Industry: {industry}")
#         print(f"Annual Revenue: {annual_revenue}")
#         print(f"Product Info: {product_info}")
#         print(f"Business Plan File: {business_plan}")
#         print(f"Financial Statements File: {financial_statements}")
#         print(f"Legal Documents File: {legal_documents}")
#         print(f"Management Profiles File: {management_profiles}")

#         # Create and save the registration if all fields are populated correctly
#         if all([business_name, ownership, tax_reg, industry, annual_revenue, product_info]):
#             registration = models.BusinessRegistration(
#                 business_name=business_name,
#                 ownership=ownership,
#                 tax_reg=tax_reg,
#                 industry=industry,
#                 annual_revenue=annual_revenue,
#                 product_info=product_info,
#                 business_plan=business_plan,
#                 financial_statements=financial_statements,
#                 legal_documents=legal_documents,
#                 management_profiles=management_profiles,
#             )
#             registration.save()

#             return HttpResponse("Business registration successful.")
#         else:
#             return HttpResponse("Error: Missing required fields.", status=400)

#     return render(request, 'BusinessREG.html')

def view_registrations(request):
    registrations = models.BusinessRegistration.objects.all()
    return render(request, 'view_registrations.html', {'registrations': registrations})