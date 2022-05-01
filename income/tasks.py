from datetime import datetime
from celery import shared_task
from user.models import Courier
from django.db.models import Q, Sum
from .models import CourierWeaklyIncome, CourierIncome


@shared_task
def weakly_income_calculation():
    to_create = []
    for courier in Courier.objects.all():
        weakly_amount = CourierIncome.objects.filter(
            Q(
                courier=courier,
                date__gt=datetime.today(),
                date__lt=datetime.today() - datetime.timedelta(days=7),
            )
        ).aggregate(sum=Sum("amount"))
        to_create.append(CourierWeaklyIncome(courier=courier, amount=weakly_amount['sum']), date=datetime.today())
    CourierWeaklyIncome.objects.bulk_create(to_create)
