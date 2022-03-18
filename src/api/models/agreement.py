from django.db import models
from datetime import date
from django.conf import settings
from simple_history.models import HistoricalRecords

class Agreement(models.Model):
    isSign = models.BooleanField(default=False)
    signature = models.CharField(max_length=300, blank=True)
    message = models.CharField(max_length=500, blank=True)
    date = models.DateField(default=date.today)

    #RELATIONS
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="agreement", on_delete=models.CASCADE)

    # HISTORY
    history = HistoricalRecords()

