# your_app/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, BusinessRegistration

class CustomUserAdmin(UserAdmin):
    # Define fields to be displayed in the admin interface
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = ('email',)
    ordering = ('email',)

    # Define fields for creating and editing users in the admin
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )

    # Remove groups and user_permissions as CustomUser does not have these fields
    filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)

# Register BusinessRegistration model
class BusinessRegistrationAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'industry', 'annual_revenue', 'submitted_at')
    search_fields = ('business_name', 'industry')
    list_filter = ('industry', 'submitted_at')

admin.site.register(BusinessRegistration, BusinessRegistrationAdmin)
class BusinessRegistrationAdmin(admin.ModelAdmin):
    list_display = ['business_name', 'ownership', 'annual_revenue', 'submitted_at']  # Use 'submitted_at' as a field
    list_filter = ['ownership', 'submitted_at']