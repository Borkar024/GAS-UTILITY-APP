from django.shortcuts import render,redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tr_url')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer service template/submit_request.html', {'form': form})

def request_tracking(request):
    service_requests = ServiceRequest.objects.all()
    return render(request, 'customer service template/track_request.html', {'service_requests': service_requests})
