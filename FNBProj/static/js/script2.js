document.getElementById('business-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const selectedBusiness = document.getElementById('business-type').value;
    
    let businessText = '';

    switch(selectedBusiness) {
        case 'sole-proprietorship':
            businessText = 'Sole Proprietorship';
            break;
        case 'partnership':
            businessText = 'Partnership';
            break;
        case 'llc':
            businessText = 'Limited Liability Company (LLC)';
            break;
        case 'corporation':
            businessText = 'Corporation (C-Corp or S-Corp)';
            break;
        case 'franchise':
            businessText = 'Franchise';
            break;
        case 'home-based-business':
            businessText = 'Home-Based Business';
            break;
        case 'e-commerce':
            businessText = 'E-commerce Business';
            break;
        case 'retail':
            businessText = 'Brick-and-Mortar Retail';
            break;
        case 'service-based':
            businessText = 'Service-Based Business';
            break;
        case 'freelancing':
            businessText = 'Freelancing';
            break;
        case 'consulting':
            businessText = 'Consulting Business';
            break;
        case 'dropshipping':
            businessText = 'Dropshipping Business';
            break;
        case 'food-truck':
            businessText = 'Food Truck';
            break;
        case 'cafe':
            businessText = 'Café or Coffee Shop';
            break;
        case 'bakery':
            businessText = 'Bakery';
            break;
        case 'boutique':
            businessText = 'Boutique';
            break;
        case 'event-planning':
            businessText = 'Event Planning';
            break;
        case 'photography':
            businessText = 'Photography Business';
            break;
        case 'pet-care':
            businessText = 'Pet Grooming or Pet Sitting';
            break;
        case 'landscaping':
            businessText = 'Landscaping or Lawn Care';
            break;
        case 'cleaning':
            businessText = 'Cleaning Services';
            break;
        case 'real-estate':
            businessText = 'Real Estate Agency';
            break;
        case 'tutoring':
            businessText = 'Tutoring Services';
            break;
        case 'fitness':
            businessText = 'Fitness Trainer or Studio';
            break;
        case 'salon':
            businessText = 'Beauty Salon or Barber Shop';
            break;
        case 'daycare':
            businessText = 'Daycare or Creche';
            break;
        case 'it-support':
            businessText = 'IT Support or Repair Services';
            break;
        case 'app-development':
            businessText = 'App Development';
            break;
        case 'handyman':
            businessText = 'Handyman Services';
            break;
        case 'digital-marketing':
            businessText = 'Digital Marketing Agency';
            break;
        case 'car-wash':
            businessText = 'Car Wash';
            break;
        case 'social-media':
            businessText = 'Social Media Management';
            break;
        case 'subscription-box':
            businessText = 'Subscription Box Service';
            break;
        case 'personal-chef':
            businessText = 'Personal Chef or Catering Service';
            break;
        case 'thrift-store':
            businessText = 'Vintage or Thrift Store';
            break;
        case 'yoga-instructor':
            businessText = 'Yoga or Meditation Instructor';
            break;
        case 'bnb':
            businessText = 'Bed and Breakfast (B&B)';
            break;
        case 'crafts':
            businessText = 'Crafts or Handmade Products Business';
            break;
        case 'interior-design':
            businessText = 'Interior Design';
            break;
        case 'translation':
            businessText = 'Translation or Interpretation Services';
            break;
        default:
            businessText = 'None';
    }
    
    document.getElementById('business-output').textContent = businessText;
});
