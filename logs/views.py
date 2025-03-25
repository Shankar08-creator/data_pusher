from django.utils.timezone import now
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import Log
from accounts.models import Account
from celery import shared_task

class DataHandlerView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        token = request.headers.get('CL-X-TOKEN')
        event_id = request.headers.get('CL-X-EVENT-ID')

        if not token:
            return Response({"success": False, "message": "Unauthenticated"}, status=401)

        try:
            account = Account.objects.get(app_secret_token=token)
        except Account.DoesNotExist:
            return Response({"success": False, "message": "Unauthenticated"}, status=401)

        log = Log.objects.create(
            event_id=event_id,
            account=account,
            received_timestamp=now(),
            received_data=request.data,
            status="pending"
        )

        send_data_to_destinations.delay(log.id)  # Asynchronous processing
        return Response({"success": True, "message": "Data Received"})
