from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.user"
    label = "core_user"
    verbose_name = _("Users")
