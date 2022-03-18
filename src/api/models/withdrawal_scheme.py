from django.db import models
from simple_history.models import HistoricalRecords
from django_currentuser.db.models import CurrentUserField
from django.conf import settings

class WithdrawalScheme(models.Model):
    name = models.CharField(max_length=100)
    totalAllowedWithdrawals = models.IntegerField()
    allowedDates = models.CharField(max_length=500)
    penaltyRate = models.FloatField()
    maxAmountAllowed = models.FloatField()
    emergencyAllowedWithdrawals = models.IntegerField()
    withdrawalInterval = models.IntegerField(default=settings.DACCOUNT_CONFIG["DEFAULT_WITHDRAWAL_INTERVAL"])  # in months
    withdrawalIntervalUnit = models.CharField(
        max_length=10,
        choices=settings.WITHDRAWAL_INTERVAL_UNIT,
        default= settings.DACCOUNT_CONFIG["DEFAULT_WITHDRAWAL_INTERVAL_UNIT"],
    )
    createdBy = CurrentUserField()
    

    def __str__(self):
        return ("%s",self.name)

    class Meta:
        ordering = ('name', )

      # HISTORY
    history = HistoricalRecords()
