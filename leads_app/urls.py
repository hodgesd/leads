from django.urls import path

from leads_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit-lead/', views.submit_lead, name='submit_lead'),
    path('manage-leads/', views.manage_leads, name='manage_leads'),
    path('update-lead-status/<int:lead_id>/', views.update_lead_status, name='update_lead_status'),
    path('delete-lead/<int:lead_id>/', views.delete_lead, name='delete_lead'),
]