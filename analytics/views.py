from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.utils import timezone

from datetime import timedelta

from django.db.models import Count

from .models import Visit

def get_visits_data(start_date, end_date):

    visits = Visit.objects.filter(entered_at__gte=start_date, entered_at__lte=end_date)
    
    # Group visits by day
    daily_data = visits.extra({'day': "strftime('%%Y-%%m-%%d', entered_at)"}).values('day').annotate(count=Count('id'))
    
    # Prepare data for charts
    chart_labels = [item['day'] for item in daily_data]
    chart_data = [item['count'] for item in daily_data]
    
    # Prepare data for the map
    country_visits = visits.values('country').annotate(visit_count=Count('id'))
    country_names = [item['country'] for item in country_visits]
    visit_data = [item['visit_count'] for item in country_visits]

    return chart_labels, chart_data, visit_data, country_names

@login_required
def dashboard(request):

    today = timezone.now()
    start_of_day = today - timedelta(days=7)  # Show data for the last 7 days
    end_of_day = today  # End with today

    chart_labels, chart_data, visit_data, country_names = get_visits_data(start_of_day, end_of_day)
    
    total_visits = sum(visit_data)

    #average_view_time = round(, 2)

    context = {
        #'average_view_time': average_view_time,
        'total_visits': total_visits,
        'chart_labels': chart_labels,
        'chart_data': chart_data,
        'visit_data': visit_data,
        'country_names': country_names,
        'start_date': start_of_day.strftime('%Y-%m-%d'),
        'end_date': end_of_day.strftime('%Y-%m-%d'),
    }
    
    return render(request, 'dashboard.html', context)

# AJAX view for date range selection
def get_data_by_date(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        
        # Convert to datetime objects
        start_date = timezone.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = timezone.datetime.strptime(end_date, '%Y-%m-%d')

        chart_labels, chart_data, visit_data, country_names = get_visits_data(start_date, end_date)
        
        total_visits = sum(visit_data)

        return JsonResponse({
            'total_visits': total_visits,
            'chart_labels': chart_labels,
            'chart_data': chart_data,
            'visit_data': visit_data,
            'country_names': country_names,
        })
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
