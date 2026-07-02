from django.contrib import admin
from .models import ContactMessage, Event, Project, Publication, BodhiShalaPublication, BodhiShalaContactMessage

admin.site.site_header = 'TATA CAIM — Admin Panel'
admin.site.site_title = 'CAIM Admin'
admin.site.index_title = 'WWelcome to TATA CAIM Admin Panel'

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'submitted_at']
    ordering = ['-submitted_at']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'time', 'venue', 'event_type']
    list_filter = ['event_type', 'date']
    search_fields = ['title', 'venue']
    ordering = ['date']
    fieldsets = [
        (None, {
            'fields': ['title', 'date', 'time', 'venue', 'event_type', 'description']
        }),
        ('Event Statistics (optional)', {
            'fields': ['registrations', 'attendees', 'teams_shortlisted', 'winning_teams'],
            'classes': ['collapse'],
        }),
    ]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'submitted_by', 'submitted_at', 'status']
    list_filter = ['status']
    search_fields = ['title']
    ordering = ['-submitted_at']
    actions = ['approve_projects']

    def approve_projects(self, request, queryset):
        queryset.update(status='approved')
    approve_projects.short_description = 'Approve selected projects'

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'authors', 'venue', 'year', 'pub_type']
    list_filter = ['pub_type', 'year']
    search_fields = ['title', 'authors']
    ordering = ['-year']

from .models import BodhiShalaPublication, BodhiShalaContactMessage

@admin.register(BodhiShalaPublication)
class BodhiShalaPublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'authors', 'venue', 'year', 'pub_type']
    list_filter = ['pub_type', 'year']
    search_fields = ['title', 'authors']
    ordering = ['-year']

@admin.register(BodhiShalaContactMessage)
class BodhiShalaContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'submitted_at']
    ordering = ['-submitted_at']