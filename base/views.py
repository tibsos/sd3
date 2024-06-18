from django.shortcuts import render, HttpResponse

from .models import *

from django.utils import timezone
from .utils import get_ip_country_city

from .models import *

def landing(request):

    url = request.META.get('HTTP_REFERER')
    ip = request.META.get('REMOTE_ADDR')

    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()

    # Check if the user agent contains keywords indicative of a mobile device
    mobile = any(keyword in user_agent for keyword in ['mobile', 'android', 'iphone', 'ipad'])

    ip, country, city = get_ip_country_city(request)
    
    Visit.objects.create(

        url = url,
        ip = ip,
        country = country,
        city = city,
        mobile = mobile,
        entered_at = timezone.now()

    )

    return render(request, 'landing.html')

def button_click(request):

    ButtonClick.objects.create()

    return HttpResponse('K')

def receive_contact_info(request):

    name = request.POST.get('n')
    phone = request.POST.get('p')

    Customer.objects.create(name = name, phone = phone)

    return HttpResponse('K')