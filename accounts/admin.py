from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User, UserOTP
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id', 'contact_number', 'email',)


# Register HomeCategory models is here.
class UserResourceAdmin(ImportExportModelAdmin, BaseUserAdmin):
    resource_class = UserResource
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    list_display = (
        'email',
        'contact_number',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined'
    )
    list_filter = (
        'is_superuser',
        'is_staff',
        'is_active'
    )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': (
            'first_name',
            'last_name',
            'dob',
            'gender',
            'contact_number',
            'platform_type')
        }),

        ('Permissions', {
            'fields': (
                'is_superuser',
                'is_active',
                'is_staff',
                'groups',
                'user_permissions',
            )}),
        ('Important dates', {'fields': ('last_login', 'date_joined')})
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'dob',
                'gender',
                'contact_number',
            )
        }
         ),
    )
    search_fields = (
        'email',
        'first_name',
        'last_name',
        'contact_number'
    )
    ordering = ('-date_joined',)
    filter_horizontal = ()


admin.site.register(User, UserResourceAdmin)


class UserOtpAdmin(admin.ModelAdmin):
    list_display = ['otp', 'user']
    search_fields = ('otp',)

    class Meta:
        model = UserOTP


admin.site.register(UserOTP, UserOtpAdmin)
