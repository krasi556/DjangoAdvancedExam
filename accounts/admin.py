# from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin
#
# from accounts.forms import NewUserChangeForm, NewUserForm
# from accounts.models import NewUser
# from django.utils.translation import gettext_lazy as _
#
# # Register your models here.
#
# UserModel = get_user_model()
#
# @admin.register(NewUser)
# class NewUserAdmin(UserAdmin):
#     add_form_template = "admin/auth/user/add_form.html"
#     change_user_password_template = None
#     fieldsets = (
#         (None, {"fields": ( "password",)}),
#         (_("Personal info"), {"fields": ("email",)}),
#         (
#             _("Permissions"),
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 ),
#             },
#         ),
#         (_("Important dates"), {"fields": ("last_login",)}),
#     )
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": ("usable_password", "password1", "password2"),
#             },
#         ),
#     )
#     form = NewUserChangeForm
#     add_form = NewUserForm
#     list_display = ( "email", "first_name", "last_name", "is_staff")
#     list_filter = ("is_staff", "is_superuser", "is_active", "groups")
#     search_fields = ( "first_name", "last_name", "email")
#     ordering = ("email",)
#     filter_horizontal = (
#         "groups",
#         "user_permissions",
#     )