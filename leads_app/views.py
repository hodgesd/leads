from django.http import HttpResponseBadRequest
from django.shortcuts import render
from .models import Lead

def home(request):
    return render(request, 'leads_app/home.html')

def submit_lead(request):
    if request.method == 'POST' and request.headers.get('HX-Request'):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        # Save the lead
        Lead.objects.create(address=address, phone=phone, email=email)

        # Render HTMX response
        return render(request, 'leads_app/lead_response.html', {'address': address, 'phone': phone, 'email': email})

    return HttpResponseBadRequest("Invalid request")