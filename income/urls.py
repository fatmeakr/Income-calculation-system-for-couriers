from django.urls import path
from .views import CourierWeaklyIncomeListView

urlpatterns = [
    path("incomes/", CourierWeaklyIncomeListView.as_view(), name="courier_incomes"),
]
