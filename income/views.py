from datetime import datetime
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import CourierWeaklyIncome
from .serializers import CourierWeaklyIncomeSerializer


class CourierWeaklyIncomeListView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CourierWeaklyIncomeSerializer

    def get(self, request, *args, **kwargs):
        from_date = self.request.GET.get("from_date")
        to_date = self.request.GET.get("to_date")
        if bool(from_date and to_date):
            try:
                from_date = datetime.strptime(from_date, '%Y/%m/%d')
                to_date = datetime.strptime(to_date, '%Y/%m/%d')
                weakly_incomes = CourierWeaklyIncome.objects.filter(
                    Q(date__lt=from_date, date__gte=to_date)
                )
                return Response(self.serializer_class(weakly_incomes, many=True).data)
            except ValueError:
                pass
        return Response(
            {"result": "bad request", "status": status.HTTP_400_BAD_REQUEST}
        )
