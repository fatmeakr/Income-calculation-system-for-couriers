from datetime import datetime
from django.db import models, transaction, IntegrityError
from django.db.models import F
from django.core.validators import MaxValueValidator


class CourierIncome(models.Model):
    courier = models.ForeignKey(
        to="user.Courier", on_delete=models.PROTECT, related_name="incomes"
    )
    date = models.DateField()
    amount = models.IntegerField(default=0)

    class Meta:
        unique_together = ['date', 'courier']

    def __str__(self):
        return f"{self.courier} : {self.date}"

    def __repr__(self):
        return self.__str__()


class PayrollDeduction(models.Model):
    courier = models.ForeignKey(
        to="user.Courier", on_delete=models.PROTECT, related_name="payroll_deductions"
    )
    amount = models.IntegerField(
        validators=[
            MaxValueValidator(-1),
        ]
    )
    description = models.CharField(max_length=1000, null=True, blank=True)
    date = models.DateField()

    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                with transaction.atomic():
                    super(PayrollDeduction, self).save(*args, **kwargs)
                    courier_income = CourierIncome.objects.select_for_update().filter(
                        courier=self.courier, date=datetime.today()
                    )
                    if courier_income:
                        courier_income.update(amount=F("amount") + self.amount)
                    else:
                        CourierIncome.objects.create(
                            courier=self.courier, amount=self.amount, date=datetime.today()
                        )
            except IntegrityError:
                raise IntegrityError('oops! something bad happend. try to add pyroll deduction again.')
        else:
            super(PayrollDeduction, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.courier} : {self.amount}"

    def __repr__(self):
        return self.__str__()


class Reward(models.Model):
    courier = models.ForeignKey(
        to="user.Courier", on_delete=models.PROTECT, related_name="rewards"
    )
    amount = models.PositiveIntegerField()
    description = models.CharField(max_length=1000, null=True, blank=True)
    date = models.DateField()

    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                with transaction.atomic():
                    super(Reward, self).save(*args, **kwargs)
                    courier_income = CourierIncome.objects.select_for_update().filter(
                        courier=self.courier, date=datetime.today()
                    )
                    if courier_income:
                        courier_income.update(amount=F("amount") + self.amount)
                    else:
                        CourierIncome.objects.create(
                            courier=self.courier, amount=self.amount, date=datetime.today()
                        )
            except IntegrityError:
                raise IntegrityError('oops! something bad happend. try to add reward again.')
        else:
            super(Reward, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.courier} : {self.amount}"

    def __repr__(self):
        return self.__str__()


class TransitCost(models.Model):
    date = models.DateField()
    amount = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                with transaction.atomic():
                    super(TransitCost, self).save(*args, **kwargs)
                    courier_income = CourierIncome.objects.select_for_update().filter(
                        courier=self.transit.courier, date=datetime.today()
                    )
                    if courier_income:
                        courier_income.update(amount=F("amount") + self.amount)
                    else:
                        CourierIncome.objects.create(
                            courier=self.transit.courier, amount=self.amount, date=datetime.today()
                        )
            except IntegrityError:
                raise IntegrityError('oops! something bad happend. try to add reward again.')
        else:
            super(TransitCost, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.amount}"

    def __repr__(self):
        return self.__str__()


class Transit(models.Model):
    class StatusType(models.IntegerChoices):
        PENDING = 0, "Pending"
        RECEIVED_TO_COURIER = 1, ""
        REJECTED = 2, "Rejected by courier"
        TOWARDS_THE_RESTURANT = 3, "Towards the resturant"
        RECEIVED = 4, "Received by courier"

    courier = models.ForeignKey(
        to="user.Courier",
        on_delete=models.PROTECT,
        related_name="transits",
    )
    business_owner = models.ForeignKey(
        to="user.BussinessOwner", on_delete=models.PROTECT, related_name="transits_of_owner"
    )
    status = models.IntegerField(choices=StatusType.choices, default=StatusType.PENDING)
    cost = models.OneToOneField(
        to=TransitCost,
        on_delete=models.PROTECT,
        related_name="transit",
    )
    created_at = models.DateField()

    def __str__(self):
        return f"{self.business_owner} - {self.courier} - {self.cost}"

    def __repr__(self):
        return self.__str__()


class CourierWeaklyIncome(models.Model):
    courier = models.ForeignKey(
        to="user.Courier", on_delete=models.PROTECT, related_name="waekly_incomes"
    )
    date = models.DateField()
    amount = models.IntegerField(default=0)

    class Meta:
        unique_together = ['date', 'courier']

    def __str__(self):
        return f"{self.courier} : {self.date}"

    def __repr__(self):
        return self.__str__()
