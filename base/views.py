from django.shortcuts import render, HttpResponse

from .models import *

from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .utils import get_ip_country_city

from django.utils.dateparse import parse_datetime

from analytics.models import *

def landing(request):

    url = request.META.get('HTTP_REFERER')
    ip = request.META.get('REMOTE_ADDR')

    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()

    # Check if the user agent contains keywords indicative of a mobile device
    mobile = any(keyword in user_agent for keyword in ['mobile', 'android', 'iphone', 'ipad'])

    ip, country, city = get_ip_country_city(request)
    
    visit = Visit.objects.create(

        url = url,
        ip = ip,
        country = country,
        city = city,
        mobile = mobile,
        entered_at = timezone.now()

    )

    return render(request, 'l_neu.html', {'i': visit.id})

@csrf_exempt
def save_leave_time(request):

    session_id = request.POST.get('i')
    leave_time = request.POST.get('t')

    visit = Visit.objects.get(id = session_id)

    visit.left_at = parse_datetime(leave_time)
    visit.save()

    return HttpResponse('K')

def button_click(request):

    ButtonClick.objects.create()

    return HttpResponse('K')

def receive_contact_info(request):

    website_type = request.POST.get('t')
    name = request.POST.get('n')
    email = request.POST.get('e')
    phone = request.POST.get('p')

    Customer.objects.create(

        website_type = website_type, 
        name = name, 
        email = email, 
        phone = phone

    )

    return HttpResponse('K')


def test(request):

    return render(request, 'test.html')