from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from import_export.admin import ExportMixin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(ExportMixin, admin.ModelAdmin):
    # Display settings
    list_display = ('email', 'phone', 'address', 'status', 'created_at')
    list_filter = ('status', 'created_at')  # Add filters for easy navigation
    search_fields = ('email', 'phone', 'address')  # Enable search functionality
    ordering = ('-created_at',)  # Default sorting (most recent first)
    readonly_fields = ('created_at',)  # Make created_at field read-only

    # Customize the form field appearance
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '40'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 60})},
    }

    # Organize fields into sections
    fieldsets = (
        ('Lead Details', {
            'fields': ('email', 'phone', 'address'),
        }),
        ('Status and Metadata', {
            'fields': ('status', 'created_at'),
            'classes': ('collapse',),  # Collapsible section
        }),
    )

    # Define custom actions
    actions = ['mark_as_contacted', 'mark_as_qualified']

    # Bulk action to mark leads as contacted
    def mark_as_contacted(self, request, queryset):
        queryset.update(status='contacted')
        self.message_user(request, f"{queryset.count()} leads marked as 'Contacted'.")

    # Bulk action to mark leads as qualified
    def mark_as_qualified(self, request, queryset):
        queryset.update(status='qualified')
        self.message_user(request, f"{queryset.count()} leads marked as 'Qualified'.")

    # Action descriptions
    mark_as_contacted.short_description = "Mark selected leads as Contacted"
    mark_as_qualified.short_description = "Mark selected leads as Qualified"