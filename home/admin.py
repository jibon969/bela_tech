from django.contrib import admin
from .models import (
    Service,
    WorkCounter,
    Project,
    Testimonial,
    Team,
    Contact,
    Replay
)


# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['title']
    search_fields = ['title']

    class Meta:
        model = Service


admin.site.register(Service, ServiceAdmin)


class WorkCounterAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['title']
    search_fields = ['title']

    class Meta:
        model = WorkCounter


admin.site.register(WorkCounter, WorkCounterAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['title', 'project_type', 'project_url']
    search_fields = ['title', 'project_type', 'project_url']

    class Meta:
        model = Project


admin.site.register(Project, ProjectAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['name']
    search_fields = ['name']

    class Meta:
        model = Testimonial


admin.site.register(Testimonial, TestimonialAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['name', 'designation']
    search_fields = ['name', 'designation']

    class Meta:
        model = Team


admin.site.register(Team, TeamAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['subject', 'name', 'phone', 'email']
    search_fields = ['subject', 'name', 'phone', 'email']

    class Meta:
        model = Contact


admin.site.register(Contact, ContactAdmin)


class ReplayAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['subject', 'send_to']
    search_fields = ['subject', 'send_to']

    class Meta:
        model = Replay


admin.site.register(Replay, ReplayAdmin)
