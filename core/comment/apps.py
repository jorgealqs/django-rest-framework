from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CommentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.comment'
    label = 'core_comment'
    verbose_name = _("Comments")
