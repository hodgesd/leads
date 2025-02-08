from django.urls import path, include
from django.contrib import admin
from leads_app import views

urlpatterns = [
    path("", include("leads_app.urls")),
    path("admin/", admin.site.urls),
    
]