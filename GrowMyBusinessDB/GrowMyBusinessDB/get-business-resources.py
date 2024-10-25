# models.py
from django.db import models

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

# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import BusinessType, BusinessResource

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

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.business_type_list, name='business_type_list'),
    path('api/resources/', views.get_business_resources, name='get_business_resources'),
]
