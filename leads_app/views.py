from datetime import datetime

from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponseBadRequest
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from .models import Lead


def home(request):
    return render(request, 'leads_app/home.html')


def submit_lead(request):
    if request.method == 'POST' and request.headers.get('HX-Request'):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        # Save the lead
        lead = Lead.objects.create(address=address, phone=phone, email=email)

        # Send notification to the team
        send_mail(
            "New Lead Submitted",
            f"New lead from {lead.email}:\n\nAddress: {lead.address}\nPhone: {lead.phone}",
            "noreply@quicksolutions.com",
            ["hodgesd@gmail.com"],
        )
        send_seller_email(lead.email, "hodgesd@gmail.com")
        # Render HTMX response
        return render(request, 'leads_app/lead_response.html', {'address': address, 'phone': phone, 'email': email})

    return HttpResponseBadRequest("Invalid request")


def send_seller_email(name, email):
    subject = "Thank You for Reaching Out!"
    context = {
        'name': name,
        'year': datetime.now().year,
    }
    message = render_to_string('leads_app/seller_notificaiton_email.html', context)
    email_message = EmailMessage(
        subject, message, 'from@example.com', [email]
    )
    email_message.content_subtype = 'html'
    email_message.send()


def manage_leads(request):
    leads = Lead.objects.all()
    return render(request, 'leads_app/manage_leads.html', {'leads': leads})

@csrf_exempt
def update_lead_status(request, lead_id):
    if request.method == "PUT":
        lead = get_object_or_404(Lead, id=lead_id)
        new_status = request.PUT.get('status')  # Use Django's request.PUT parser
        lead.status = new_status
        lead.save()
        return JsonResponse({'status': 'success', 'new_status': lead.status})

@csrf_exempt
def delete_lead(request, lead_id):
    if request.method == "DELETE":
        lead = get_object_or_404(Lead, id=lead_id)
        lead.delete()
        return JsonResponse({'status': 'success'})