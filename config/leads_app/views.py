from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'leads_app/home.html')

def submit_lead(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        # Simulate saving data or other processing
        print(f"New lead: {address}, {phone}, {email}")

        # Check if request is from HTMX
        if request.headers.get('HX-Request'):
            return render(request, 'templates/lead_response.html')

        # Fallback for non-HTMX requests
        return JsonResponse({'message': "Thank you! We'll be in touch soon."})

    return JsonResponse({'error': 'Invalid request'}, status=400)