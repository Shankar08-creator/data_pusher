from celery import shared_task
import requests
from .models import Log, Destination
from django.utils.timezone import now

@shared_task
def send_data_to_destinations(log_id):
    log = Log.objects.get(id=log_id)
    destinations = log.account.destinations.all()

    for destination in destinations:
        try:
            headers = destination.headers
            if destination.http_method == 'GET':
                response = requests.get(destination.url, headers=headers, params=log.received_data)
            else:
                response = requests.request(destination.http_method, destination.url, headers=headers, json=log.received_data)

            log.status = "success" if response.status_code == 200 else "failed"
        except Exception:
            log.status = "failed"

        log.processed_timestamp = now()
        log.save()
