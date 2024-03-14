from django.contrib.admin import SimpleListFilter
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class CreatedDateFilter(SimpleListFilter):
    title = _('Created Date')
    parameter_name = 'created_date'

    def lookups(self, request, model_admin):
        return (
            ('today', _('Today')),
            ('week', _('This week')),
            ('month', _('This month')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'today':
            return queryset.filter(created__date=timezone.now().date())
        elif self.value() == 'week':
            start_of_week = timezone.now().date() - timezone.timedelta(days=timezone.now().weekday())
            end_of_week = start_of_week + timezone.timedelta(days=6)
            return queryset.filter(created__date__range=[start_of_week, end_of_week])
        elif self.value() == 'month':
            return queryset.filter(created__year=timezone.now().year, created__month=timezone.now().month)
        else:
            return queryset
