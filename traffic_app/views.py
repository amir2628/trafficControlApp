from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import TrafficLightConfiguration
from .forms import TrafficLightForm

# def control_dashboard(request):
    # # Retrieve the configuration; if it doesn't exist, create one with default values.
    # config, created = TrafficLightConfiguration.objects.get_or_create(id=1)
    
    # # Calculate the next state using the model's method.
    # next_state = config.next_state()

    # # Process form submission.
    # if request.method == 'POST':
    #     form = TrafficLightForm(request.POST, instance=config)
    #     if form.is_valid():
    #         form.save()
    #         # Redirect to avoid resubmission.
    #         return redirect('control_dashboard')
    # else:
    #     form = TrafficLightForm(instance=config)

    # context = {
    #     'form': form,
    #     'config': config,
    #     'next_state': next_state,
    #     'page_title': 'Traffic Light Control Dashboard',
    # }
    # return render(request, 'traffic_app/control.html', context)
def control_dashboard(request):
    config = TrafficLightConfiguration.objects.get_or_create(id=1)[0]
    form = TrafficLightForm(instance=config)
    next_state = config.next_state()
    
    if request.method == 'POST':
        form = TrafficLightForm(request.POST, instance=config)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'red_duration': config.red_duration,
                    'yellow_duration': config.yellow_duration,
                    'green_duration': config.green_duration,
                    'current_state': config.current_state,
                    'last_updated': config.last_updated.strftime('%Y-%m-%d %H:%M:%S')
                })
            return redirect('control_dashboard')
        # If form is invalid, continue to render the page with errors

    context = {
        'form': form,
        'config': config,
        'next_state': next_state,
        'page_title': 'Traffic Light Control Dashboard',
    }
    return render(request, 'traffic_app/control.html', context)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def update_state(request):
    config = TrafficLightConfiguration.objects.get(id=1)
    config.current_state = config.next_state()
    config.save()
    return JsonResponse({
        'current_state': config.current_state,
        'last_updated': config.last_updated.strftime('%Y-%m-%d %H:%M:%S')
    })