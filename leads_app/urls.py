from django.urls import path

from leads_app import views
urlpatterns = [
    path('', views.home, name='home'),
    path('submit-lead/', views.submit_lead, name='submit_lead'),
]