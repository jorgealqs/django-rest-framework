from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from core.user.models import User
from core.user.forms import UserAdminChangeForm
# from core.user.forms import UserAdminCreationForm


@admin.action(description="Mark selected stories as published")
def make_published(modeladmin, request, queryset):
    print(f"\n\n make_published -> {queryset} \n\n ")

@admin.action(description="Other test")
def other_test(modeladmin, request, queryset):
    print(f"\n\n other_test -> {queryset} \n\n ")

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  form = UserAdminChangeForm
  # add_form = UserAdminCreationForm
  # fields = ('username', 'first_name', 'last_name',)
  # fieldsets = ('email',)
  fieldsets = (
      (
        _("Auth"),
        {"fields": (
          "email",
          "password"
          )
        }
      ),
      (
        _("Personal info"),
        {"fields": (
          "username",
          "first_name",
          "last_name",
          "bio",
          "avatar",
          )
        }
      ),
      (
        _("Permissions"),
        {
          "fields": (
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
          ),
        },
      ),
      (
        _("Important dates"),
        {"fields": (
            "last_login",
          )
        }
      ),
  )

  list_display = (
    'email',
    'first_name',
    'last_name',
    'is_active',
    'is_staff',
    'is_superuser',
  )

  list_display_links = ["email", "first_name"]
  search_fields = ["first_name", "last_name"]
  list_filter = ["is_active", "is_staff"]
  filter_horizontal = ["user_permissions", "groups",]
  # list_editable = ('is_active', 'first_name',)
  actions = [make_published, other_test]
  ordering = ["id"]
  # add_fieldsets = (
  #   (
  #     None,
  #     {
  #         "classes": ("wide",),
  #         "fields": ("email", "password1", "password2"),
  #     },
  #   ),
  # )
