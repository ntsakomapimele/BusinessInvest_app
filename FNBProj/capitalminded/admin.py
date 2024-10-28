from django.contrib import admin
from .models import (
    BusinessRegistration,
    CustomUser ,
    BusinessType,
    BusinessResource,
    MicroLoan,
    LoanPayment,
    Investment  # Don't forget to import the Investment model
)

# BusinessRegistration Admin
@admin.register(BusinessRegistration)
class BusinessRegistrationAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'industry', 'annual_revenue', 'submitted_at')
    search_fields = ('business_name', 'industry')
    list_filter = ('industry', 'submitted_at')
    date_hierarchy = 'submitted_at'

# CustomUser  Admin
@admin.register(CustomUser )
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    list_filter = ('is_active', 'is_staff', 'is_superuser')

# BusinessType Admin
@admin.register(BusinessType)
class BusinessTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

# BusinessResource Admin
@admin.register(BusinessResource)
class BusinessResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'business_type', 'order')
    list_filter = ('business_type',)
    search_fields = ('title', 'description')

# MicroLoan Admin
@admin.register(MicroLoan)
class MicroLoanAdmin(admin.ModelAdmin):
    list_display = ('business', 'amount_requested', 'status', 'application_date', 'remaining_balance')
    list_filter = ('status', 'payment_frequency')
    search_fields = ('business__business_name', 'purpose')
    date_hierarchy = 'application_date'
    readonly_fields = ('total_amount', 'total_interest', 'performance_score')

    fieldsets = (
        ('Basic Information', {
            'fields': ('business', 'amount_requested', 'interest_rate', 'term_months', 'purpose')
        }),
        ('Status and Dates', {
            'fields': ('status', 'application_date', 'approval_date', 'start_date', 'end_date')
        }),
        ('Payment Information', {
            'fields': ('monthly_payment', 'payment_frequency', 'next_payment_date', 'remaining_balance')
        }),
        ('Performance', {
            'fields': ('performance_score', 'principal_paid', 'interest_paid', 'total_payments_made')
        }),
    )

# LoanPayment Admin
@admin.register(LoanPayment)
class LoanPaymentAdmin(admin.ModelAdmin):
    list_display = ('loan', 'amount', 'payment_date', 'status', 'transaction_id')
    list_filter = ('status', 'payment_date')
    search_fields = ('loan__business__business_name', 'transaction_id')
    date_hierarchy = 'payment_date'
    readonly_fields = ('total_amount',)

    fieldsets = (
        ('Payment Information', {
            'fields': ('loan', 'amount', 'payment_date', 'status', 'transaction_id')
        }),
        ('Amount Breakdown', {
            'fields': ('principal_amount', 'interest_amount', 'due_date')
        }),
        ('Additional Information', {
            'fields': ('notes',)
        }),
    )

# Investment Admin
@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('investor', 'business', 'shares', 'amount')
    search_fields = ('investor__email', 'business__business_name')
    list_filter = ('business',)