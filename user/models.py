from django.db import models
from django.contrib.auth.models import User


class Courier(models.Model):
    user = models.OneToOneField(
        to=User, on_delete=models.PROTECT, related_name="courier"
    )

    def __str__(self):
        return f"{self.user}"

    def __repr__(self):
        return self.__str__()


class BussinessOwner(models.Model):
    user = models.OneToOneField(
        to=User, on_delete=models.PROTECT, related_name="bussiness_owner"
    )

    def __str__(self):
        return f"{self.user}"

    def __repr__(self):
        return self.__str__()
