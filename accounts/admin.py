from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User, Buyer


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_superuser', 'is_staff', 'is_active', 'is_buyer', 'is_moderator')
    list_filter = ('is_superuser', 'is_staff', 'is_active', 'is_buyer', 'is_moderator')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'dob', 'gender', 'contact_number')}),
        ('Permissions', {'fields': (
        'is_superuser', 'is_active', 'is_staff', 'is_buyer', 'is_moderator', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')})
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'dob', 'gender', 'contact_number')
        }
         ),
    )
    search_fields = ('email', 'first_name', 'last_name',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)


class BuyerAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_buyer']
    list_filter = ['user__is_buyer']
    search_fields = ('user__email', 'user__first_name', 'user__last_name',)

    def is_buyer(self, obj):
        return obj.user.is_buyer

    is_buyer.short_description = 'Buyer'
    is_buyer.admin_order_field = 'user__is_buyer'


admin.site.register(Buyer, BuyerAdmin)

# Remove Group Model from admin. We're not using it.
# admin.site.unregister(Group)
