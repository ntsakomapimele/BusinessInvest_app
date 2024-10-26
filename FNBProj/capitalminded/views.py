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
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Get the next parameter or default to dashboard
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
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

# views.py
from django.db.models import Sum, Q
from django.utils import timezone
from datetime import timedelta

# capitalminded/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Avg
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal
from .models import BusinessRegistration, MicroLoan, LoanPayment

@login_required
def business_overview(request, business_id):
    company = get_object_or_404(BusinessRegistration, id=business_id)
    
    # Get all loans with filters
    status_filter = request.GET.get('status', 'all')
    if status_filter != 'all':
        loans = MicroLoan.objects.filter(business=company, status=status_filter)
    else:
        loans = MicroLoan.objects.filter(business=company)

    # Calculate loan statistics
    loan_stats = {
        'total_borrowed': loans.aggregate(Sum('amount_requested'))['amount_requested__sum'] or 0,
        'active_loans': loans.filter(status='ACTIVE').count(),
        'total_outstanding': loans.filter(status='ACTIVE').aggregate(Sum('remaining_balance'))['remaining_balance__sum'] or 0,
        'upcoming_payments': loans.filter(
            status='ACTIVE',
            next_payment_date__lte=timezone.now().date() + timedelta(days=7)
        ).order_by('next_payment_date'),
    }

    # Get payment history
    payment_history = LoanPayment.objects.filter(
        loan__business=company
    ).select_related('loan').order_by('-payment_date')[:10]

    # Calculate overall performance metrics
    performance_metrics = {
        'on_time_payment_rate': calculate_on_time_payment_rate(company),
        'avg_performance_score': calculate_avg_performance_score(company),
        'total_paid_off_loans': loans.filter(status='PAID').count(),
    }

    context = {
        'company': company,
        'loans': loans,
        'loan_stats': loan_stats,
        'payment_history': payment_history,
        'performance_metrics': performance_metrics,
        'status_filter': status_filter,
    }
    
    return render(request, 'business_page.html', context)

def calculate_on_time_payment_rate(company):
    total_payments = LoanPayment.objects.filter(loan__business=company).count()
    if total_payments == 0:
        return 100
    on_time_payments = LoanPayment.objects.filter(
        loan__business=company,
        status='COMPLETED',
        payment_date__lte=models.F('loan__next_payment_date')
    ).count()
    return (on_time_payments / total_payments) * 100

def calculate_avg_performance_score(company):
    loans = MicroLoan.objects.filter(business=company)
    if not loans.exists():
        return 100
    return loans.aggregate(Avg('performance_score'))['performance_score__avg']

@login_required
def loan_payment_history(request, loan_id):
    loan = get_object_or_404(MicroLoan, id=loan_id)
    payments = loan.payments.all().order_by('-payment_date')
    return render(request, 'loan_payment_history.html', {'loan': loan, 'payments': payments})

@login_required
def make_loan_payment(request, loan_id):
    if request.method == 'POST':
        loan = get_object_or_404(MicroLoan, id=loan_id)
        amount = Decimal(request.POST.get('amount'))
        
        payment = LoanPayment.objects.create(
            loan=loan,
            amount=amount,
            status='COMPLETED'
        )
        
        # Update loan balance
        loan.remaining_balance -= amount
        loan.total_payments_made += amount
        loan.next_payment_date = calculate_next_payment_date(loan)
        loan.performance_score = loan.calculate_performance_score()
        loan.update_loan_status()
        
        messages.success(request, f'Payment of ${amount} successfully processed')
        return redirect('loan_status', loan_id=loan_id)

    return render(request, 'make_payment.html', {'loan': loan})