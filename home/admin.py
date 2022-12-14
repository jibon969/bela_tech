from django.contrib import admin
from .models import (
    Slider,
    Service,
    WorkCounter,
    Project,
    Testimonial,
    Team,
    Contact,
    Replay
)


# Register your models here.
class SliderAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['title']
    search_fields = ['title']

    class Meta:
        model = Slider


admin.site.register(Slider, SliderAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['title', 'value', 'timestamp']
    search_fields = ['title']
    list_editable = ['value']

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
    list_display = ['title', 'project_type', 'project_url', 'value', 'timestamp']
    search_fields = ['title', 'project_type', 'project_url']
    list_editable = ['value']

    class Meta:
        model = Project


admin.site.register(Project, ProjectAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['name', 'value', 'timestamp']
    search_fields = ['name']
    list_editable = ['value']

    class Meta:
        model = Testimonial


admin.site.register(Testimonial, TestimonialAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['name', 'designation', 'value', 'timestamp']
    search_fields = ['name', 'designation']
    list_editable = ['value']

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
