from django.db import models
from django.conf import settings
from django_currentuser.db.models import CurrentUserField
from simple_history.models import HistoricalRecords

class Customer(models.Model):
    home_phone = models.CharField(max_length=20, blank=True)
    emergency_phone = models.CharField(max_length=20)
    creator = CurrentUserField()

    # Relationships of entities
    
    # user can be a customer
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name = "customer_details"
    )

      # HISTORY
    history = HistoricalRecords()
