class Log(models.Model):
    event_id = models.UUIDField(default=uuid.uuid4, unique=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    received_timestamp = models.DateTimeField(auto_now_add=True)
    processed_timestamp = models.DateTimeField(null=True, blank=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    received_data = models.JSONField()
    status = models.CharField(max_length=10, choices=[('success', 'Success'), ('failed', 'Failed')])
