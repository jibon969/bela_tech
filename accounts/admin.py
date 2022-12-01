# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.admin import GroupAdmin
# from django.contrib.auth.models import Group
#
# from .forms import UserAdminCreationForm, UserAdminChangeForm
# from .models import User, Buyer, UserOTP
# from import_export import resources
# from import_export.admin import ImportExportModelAdmin
#
#
# class UserResource(resources.ModelResource):
#     class Meta:
#         model = User
#
#         fields = ('id', 'contact_number', 'email',)
#
#
# # Register HomeCategory models is here.
# class UserResourceAdmin(ImportExportModelAdmin, BaseUserAdmin):
#     resource_class = UserResource
#     form = UserAdminChangeForm
#     add_form = UserAdminCreationForm
#     list_display = ('email', 'contact_number', 'is_superuser', 'is_staff',
#                     'is_active', 'is_moderator', 'date_joined')
#     list_filter = ('is_superuser', 'is_staff', 'is_active', 'is_moderator', 'is_dashboard')
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'dob', 'gender', 'contact_number', 'platform_type')}),
#         ('Permissions', {'fields': ('is_superuser', 'is_active', 'is_staff', 'is_buyer',
#                                     'is_moderator', 'groups', 'user_permissions', 'is_dashboard')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')})
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2', 'first_name',
#                        'last_name', 'dob', 'gender', 'contact_number', 'platform_type',)
#         }
#          ),
#     )
#     search_fields = ('email', 'first_name', 'last_name', 'contact_number', 'platform_type')
#     ordering = ('-date_joined',)
#     filter_horizontal = ()
#
#
# admin.site.register(User, UserResourceAdmin)
#
#
# class BuyerAdmin(admin.ModelAdmin):
#     list_display = ['user', 'is_buyer']
#     list_filter = ['user__is_buyer']
#     search_fields = ('user__email', 'user__first_name', 'user__last_name',)
#
#     def is_buyer(self, obj):
#         return obj.user.is_buyer
#
#     is_buyer.short_description = 'Buyer'
#     is_buyer.admin_order_field = 'user__is_buyer'
#
#
# admin.site.register(Buyer, BuyerAdmin)
#
#
# class UserOtpAdmin(admin.ModelAdmin):
#     list_display = ['otp', 'user']
#     search_fields = ('otp',)
#
#     class Meta:
#         model = UserOTP
#
#
# admin.site.register(UserOTP, UserOtpAdmin)
#
#
# class GroupsAdmin(admin.ModelAdmin):
#     list_display = ["name", "pk"]
#
#     class Meta:
#         model = Group
#
#
# admin.site.unregister(Group)
# admin.site.register(Group, GroupsAdmin)


from django.contrib import admin
from .models import User, EmailActivation
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'dob', 'gender', 'contact_number']
    search_fields = ['first_name', 'last_name', 'email', 'dob', 'gender', 'contact_number']
    list_per_page = 20

    class Meta:
        model = User


admin.site.register(User, UserAdmin)


class EmailActivationAdmin(admin.ModelAdmin):
    list_display = ['user', 'email']
    list_per_page = 20
    search_fields = ['email']

    class Meta:
        model = EmailActivation


admin.site.register(EmailActivation, EmailActivationAdmin)
