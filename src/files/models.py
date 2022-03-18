from django.db import models
from django_currentuser.db.models import CurrentUserField
from simple_history.models import HistoricalRecords

class File(models.Model):
  file = models.FileField(blank=False, null=False)
  purpose = models.CharField(max_length=100)
  timestamp = models.DateTimeField(auto_now_add=True)
  owner = CurrentUserField()
     # HISTORY
  history = HistoricalRecords()
