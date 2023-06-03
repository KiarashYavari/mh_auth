from django.contrib import admin
from mh_auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class MHUserAdmin(UserAdmin):
  fieldsets = (
        (None, {"fields": ("email", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
  add_fieldsets = (
      (
          None,
          {
              "classes": ("wide",),
              "fields": ("email", "password1", "password2"),
          },
      ),
  )
  list_display = ("email", "first_name", "last_name", "is_staff")
  search_fields = ("email", "first_name", "last_name")
  ordering = ("email",)

admin.site.register(User, MHUserAdmin)

