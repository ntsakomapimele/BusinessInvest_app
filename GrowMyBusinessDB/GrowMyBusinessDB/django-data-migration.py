# migrations/0002_initial_data.py
from django.db import migrations

def create_initial_data(apps, schema_editor):
    BusinessType = apps.get_model('your_app_name', 'BusinessType')
    BusinessResource = apps.get_model('your_app_name', 'BusinessResource')
    
	 # Sole Proprietorship
    sole_proprietorship = BusinessType.objects.create(
        name='Sole Proprietorship',
        slug='sole-proprietorship',
        description='Resources for sole proprietorship businesses'
    )
    BusinessResource.objects.create(
        business_type=sole_proprietorship,
        title='Sole Proprietorship Guide',
        url='https://www.soleproprietorshipguide.com',
        description='Guide on starting a sole proprietorship',
        order=1
    )

    # Partnership
    partnership = BusinessType.objects.create(
        name='Partnership',
        slug='partnership',
        description='Resources for partnership businesses'
    )
    BusinessResource.objects.create(
        business_type=partnership,
        title='Partnership Agreement Templates',
        url='https://www.partnershiptemplates.com',
        description='Templates and resources for partnerships',
        order=1
    )

    # LLC
    llc = BusinessType.objects.create(
        name='Limited Liability Company (LLC)',
        slug='llc',
        description='Resources for LLC businesses'
    )
    BusinessResource.objects.create(
        business_type=llc,
        title='LLC Formation Resources',
        url='https://www.llcresources.com',
        description='Tools and resources for forming an LLC',
        order=1
    )

    # Corporation
    corporation = BusinessType.objects.create(
        name='Corporation (C-Corp or S-Corp)',
        slug='corporation',
        description='Resources for corporation businesses'
    )
    BusinessResource.objects.create(
        business_type=corporation,
        title='Corporate Governance Guidelines',
        url='https://www.corporategovernance.com',
        description='Best practices for C-Corps and S-Corps',
        order=1
    )

    # Franchise
    franchise = BusinessType.objects.create(
        name='Franchise',
        slug='franchise',
        description='Resources for franchise businesses'
    )
    BusinessResource.objects.create(
        business_type=franchise,
        title='Franchise Opportunities Directory',
        url='https://www.franchisedirectory.com',
        description='Directory of franchise opportunities and resources',
        order=1
    )

    # Home-Based Business
    home_based = BusinessType.objects.create(
        name='Home-Based Business',
        slug='home-based-business',
        description='Resources for home-based businesses'
    )
    BusinessResource.objects.create(
        business_type=home_based,
        title='Home-Based Business Tips',
        url='https://www.homebasedbusinesstips.com',
        description='Tips for starting and running a home-based business',
        order=1
    )

    # E-commerce Business
    e_commerce = BusinessType.objects.create(
        name='E-commerce Business',
        slug='e-commerce',
        description='Resources for e-commerce businesses'
    )
    BusinessResource.objects.create(
        business_type=e_commerce,
        title='E-commerce Platform Comparison',
        url='https://www.ecommerceplatforms.com',
        description='Comparison of e-commerce platforms and tools',
        order=1
    )

    # Brick-and-Mortar Retail
    retail = BusinessType.objects.create(
        name='Brick-and-Mortar Retail',
        slug='retail',
        description='Resources for physical retail businesses'
    )
    BusinessResource.objects.create(
        business_type=retail,
        title='Retail Store Setup Guide',
        url='https://www.retailstoreguide.com',
        description='Guide on setting up a brick-and-mortar store',
        order=1
    )

    # Service-Based Business
    service_based = BusinessType.objects.create(
        name='Service-Based Business',
        slug='service-based',
        description='Resources for service-based businesses'
    )
    BusinessResource.objects.create(
        business_type=service_based,
        title='Service Business Best Practices',
        url='https://www.servicebusinesspractices.com',
        description='Best practices for service-based businesses',
        order=1
    )

    # Freelancing
    freelancing = BusinessType.objects.create(
        name='Freelancing',
        slug='freelancing',
        description='Resources for freelancing businesses'
    )
    BusinessResource.objects.create(
        business_type=freelancing,
        title='Freelancing Platforms and Tools',
        url='https://www.freelancingtools.com',
        description='Tools and platforms for freelancers',
        order=1
    )

    # Consulting Business
    consulting = BusinessType.objects.create(
        name='Consulting Business',
        slug='consulting',
        description='Resources for consulting businesses'
    )
    BusinessResource.objects.create(
        business_type=consulting,
        title='Consulting Success Strategies',
        url='https://www.consultingsuccess.com',
        description='Strategies and resources for consultants',
        order=1
    )

    # Dropshipping Business
    dropshipping = BusinessType.objects.create(
        name='Dropshipping Business',
        slug='dropshipping',
        description='Resources for dropshipping businesses'
    )
    BusinessResource.objects.create(
        business_type=dropshipping,
        title='Dropshipping Suppliers Directory',
        url='https://www.dropshippingsuppliers.com',
        description='Directory of dropshipping suppliers',
        order=1
    )
    
	
    # Create business type
    bakery = BusinessType.objects.create(
        name='Bakery',
        slug='bakery',
        description='Resources for starting and growing a bakery business'
    )
    
    # Create resources for bakery
    BusinessResource.objects.create(
        business_type=bakery,
        title='Bakery Federation',
        url='https://www.bakeryfederation.org',
        description='Industry news, training, and certification resources',
        order=1
    )
    BusinessResource.objects.create(
        business_type=bakery,
        title='Bakery Equipment Suppliers',
        url='https://www.bakerypros.com',
        description='Professional bakery equipment and supplies',
        order=2
    )
      # Food Truck
    food_truck = BusinessType.objects.create(
        name='Food Truck',
        slug='food-truck',
        description='Resources for starting and running a food truck business'
    )
    BusinessResource.objects.create(
        business_type=food_truck,
        title='Food Truck Association',
        url='https://www.foodtruckassociation.com',
        description='Resources for food truck regulations and setup',
        order=1
    )

    # Café or Coffee Shop
    cafe = BusinessType.objects.create(
        name='Café or Coffee Shop',
        slug='cafe',
        description='Resources for opening a café or coffee shop'
    )
    BusinessResource.objects.create(
        business_type=cafe,
        title='Coffee Shop Startup Guide',
        url='https://www.coffeeshopstartup.com',
        description='Guide for starting a coffee shop business',
        order=1
    )

    # Bakery
    bakery = BusinessType.objects.create(
        name='Bakery',
        slug='bakery',
        description='Resources for starting and growing a bakery business'
    )
    BusinessResource.objects.create(
        business_type=bakery,
        title='Bakery Federation',
        url='https://www.bakeryfederation.org',
        description='Industry news, training, and certification resources',
        order=1
    )

    # Boutique
    boutique = BusinessType.objects.create(
        name='Boutique',
        slug='boutique',
        description='Resources for running a boutique'
    )
    BusinessResource.objects.create(
        business_type=boutique,
        title='Boutique Owner’s Guide',
        url='https://www.boutiqueowners.com',
        description='Guide to running a successful boutique',
        order=1
    )

    # Event Planning
    event_planning = BusinessType.objects.create(
        name='Event Planning',
        slug='event-planning',
        description='Resources for event planning businesses'
    )
    BusinessResource.objects.create(
        business_type=event_planning,
        title='Event Planning Resources',
        url='https://www.eventplanningresources.com',
        description='Event planning tips and strategies',
        order=1
    )

    # Photography Business
    photography = BusinessType.objects.create(
        name='Photography Business',
        slug='photography',
        description='Resources for starting a photography business'
    )
    BusinessResource.objects.create(
        business_type=photography,
        title='Photography Business Guide',
        url='https://www.photographybusiness.com',
        description='Guide to starting a photography business',
        order=1
    )

    # Pet Grooming or Pet Sitting
    pet_care = BusinessType.objects.create(
        name='Pet Grooming or Pet Sitting',
        slug='pet-care',
        description='Resources for pet grooming or sitting businesses'
    )
    BusinessResource.objects.create(
        business_type=pet_care,
        title='Pet Care Business Resources',
        url='https://www.petcarebusiness.com',
        description='Resources for pet grooming and sitting businesses',
        order=1
    )

    # Landscaping or Lawn Care
    landscaping = BusinessType.objects.create(
        name='Landscaping or Lawn Care',
        slug='landscaping',
        description='Resources for landscaping and lawn care businesses'
    )
    BusinessResource.objects.create(
        business_type=landscaping,
        title='Landscaping Business Tips',
        url='https://www.landscapingbusiness.com',
        description='Tips for running a landscaping business',
        order=1
    )

    # Cleaning Services
    cleaning = BusinessType.objects.create(
        name='Cleaning Services',
        slug='cleaning',
        description='Resources for cleaning service businesses'
    )
    BusinessResource.objects.create(
        business_type=cleaning,
        title='Cleaning Business Resources',
        url='https://www.cleaningbusiness.com',
        description='Resources for starting a cleaning service',
        order=1
    )

    # Real Estate Agency
    real_estate = BusinessType.objects.create(
        name='Real Estate Agency',
        slug='real-estate',
        description='Resources for real estate businesses'
    )
    BusinessResource.objects.create(
        business_type=real_estate,
        title='Real Estate Business Resources',
        url='https://www.realestatebusiness.com',
        description='Resources for running a real estate agency',
        order=1
    )

    # Tutoring Services
    tutoring = BusinessType.objects.create(
        name='Tutoring Services',
        slug='tutoring',
        description='Resources for tutoring businesses'
    )
    BusinessResource.objects.create(
        business_type=tutoring,
        title='Tutoring Business Tips',
        url='https://www.tutoringbusiness.com',
        description='Tips for starting a tutoring service',
        order=1
    )

    # Fitness Trainer or Studio
    fitness = BusinessType.objects.create(
        name='Fitness Trainer or Studio',
        slug='fitness',
        description='Resources for fitness trainers and studios'
    )
    BusinessResource.objects.create(
        business_type=fitness,
        title='Fitness Business Resources',
        url='https://www.fitnessbusiness.com',
        description='Resources for fitness trainers and studios',
        order=1
    )

    # Beauty Salon or Barber Shop
    salon = BusinessType.objects.create(
        name='Beauty Salon or Barber Shop',
        slug='salon',
        description='Resources for beauty salons and barber shops'
    )
    BusinessResource.objects.create(
        business_type=salon,
        title='Salon Business Tips',
        url='https://www.salonbusiness.com',
        description='Tips for running a salon or barber shop',
        order=1
    )

    # Daycare or Creche
    daycare = BusinessType.objects.create(
        name='Daycare or Creche',
        slug='daycare',
        description='Resources for daycare and creche businesses'
    )
    BusinessResource.objects.create(
        business_type=daycare,
        title='Daycare Business Resources',
        url='https://www.daycarebusiness.com',
        description='Resources for running a daycare',
        order=1
    )

    # IT Support or Repair Services
    it_support = BusinessType.objects.create(
        name='IT Support or Repair Services',
        slug='it-support',
        description='Resources for IT support and repair businesses'
    )
    BusinessResource.objects.create(
        business_type=it_support,
        title='IT Support Business Resources',
        url='https://www.itsupportbusiness.com',
        description='Resources for starting an IT support business',
        order=1
    )

    # App Development
    app_development = BusinessType.objects.create(
        name='App Development',
        slug='app-development',
        description='Resources for app development businesses'
    )
    BusinessResource.objects.create(
        business_type=app_development,
        title='App Development Tools',
        url='https://www.appdevtools.com',
        description='Resources for app developers',
        order=1
    )

    # Handyman Services
    handyman = BusinessType.objects.create(
        name='Handyman Services',
        slug='handyman',
        description='Resources for handyman businesses'
    )
    BusinessResource.objects.create(
        business_type=handyman,
        title='Handyman Business Resources',
        url='https://www.handymanbusiness.com',
        description='Resources for running a handyman business',
        order=1
    )

    # Digital Marketing Agency
    digital_marketing = BusinessType.objects.create(
        name='Digital Marketing Agency',
        slug='digital-marketing',
        description='Resources for digital marketing agencies'
    )
    BusinessResource.objects.create(
        business_type=digital_marketing,
        title='Digital Marketing Resources',
        url='https://www.digitalmarketingresources.com',
        description='Resources for digital marketers',
        order=1
    )

    # Car Wash
    car_wash = BusinessType.objects.create(
        name='Car Wash',
        slug='car-wash',
        description='Resources for car wash businesses'
    )
    BusinessResource.objects.create(
        business_type=car_wash,
        title='Car Wash Business Guide',
        url='https://www.carwashbusiness.com',
        description='Guide to running a successful car wash business',
        order=1
    )

    # Social Media Management
    social_media = BusinessType.objects.create(
        name='Social Media Management',
        slug='social-media',
        description='Resources for social media management businesses'
    )
    BusinessResource.objects.create(
        business_type=social_media,
        title='Social Media Management Tools',
        url='https://www.socialmediamanagement.com',
        description='Tools for social media management professionals',
        order=1
    )

    # Subscription Box Service
    subscription_box = BusinessType.objects.create(
        name='Subscription Box Service',
        slug='subscription-box',
        description='Resources for subscription box businesses'
    )
    BusinessResource.objects.create(
        business_type=subscription_box,
        title='Subscription Box Resources',
        url='https://www.subscriptionboxresources.com',
        description='Resources for creating a subscription box service',
        order=1
    )

    # Personal Chef or Catering Service
    personal_chef = BusinessType.objects.create(
        name='Personal Chef or Catering Service',
        slug='personal-chef',
        description='Resources for personal chefs and catering services'
    )

	  # Crafts or Handmade Products Business
    crafts = BusinessType.objects.create(
        name='Crafts or Handmade Products Business',
        slug='crafts',
        description='Resources for starting a crafts or handmade products business'
    )
    BusinessResource.objects.create(
        business_type=crafts,
        title='Handmade Business Guide',
        url='https://www.handmadebusiness.com',
        description='Guide to running a successful handmade products business',
        order=1
    )

    # Interior Design
    interior_design = BusinessType.objects.create(
        name='Interior Design',
        slug='interior-design',
        description='Resources for starting an interior design business'
    )
    BusinessResource.objects.create(
        business_type=interior_design,
        title='Interior Design Business Resources',
        url='https://www.interiorbusiness.com',
        description='Resources for interior designers to grow their business',
        order=1
    )

    # Translation or Interpretation Services
    translation = BusinessType.objects.create(
        name='Translation or Interpretation Services',
        slug='translation',
        description='Resources for running a translation or interpretation business'
    )
    BusinessResource.objects.create(
        business_type=translation,
        title='Translation Business Guide',
        url='https://www.translationbusiness.com',
        description='Guide to starting a translation or interpretation business',
        order=1
    )
	
	
def remove_initial_data(apps, schema_editor):
    BusinessType = apps.get_model('your_app_name', 'BusinessType')
    BusinessType.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('your_app_name', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data, remove_initial_data),
    ]
