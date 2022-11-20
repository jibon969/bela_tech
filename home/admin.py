from django.contrib import admin
from .models import Contact, Replay


# Register your models here.
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
