from django.contrib import admin
from django.contrib.auth.models import Group
from django_celery_beat.models import (
    SolarSchedule,
    IntervalSchedule,
    ClockedSchedule,
    CrontabSchedule,
)
from .models import Transit, TransitCost, PayrollDeduction, Reward, CourierIncome, CourierWeaklyIncome


class TransitInline(admin.TabularInline):
    model = Transit
    extra = 0
    min_num = 1


@admin.register(TransitCost)
class TransitCostAdmin(admin.ModelAdmin):
    inlines = [TransitInline]
    readonly_fields = ["date"]


admin.site.register(PayrollDeduction)
admin.site.register(Reward)
admin.site.register(CourierIncome)
admin.site.register(CourierWeaklyIncome)

# unregister
admin.site.unregister(Group)
admin.site.unregister(SolarSchedule)
admin.site.unregister(ClockedSchedule)
admin.site.unregister(IntervalSchedule)
admin.site.unregister(CrontabSchedule)
