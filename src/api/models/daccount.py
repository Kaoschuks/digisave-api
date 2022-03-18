from django.db import models
from api.models.customer import Customer
# from api.models.branch import *
# from api.models.employee import *
# from api.models.report_scheme import *
from api.models.withdrawal_scheme import WithdrawalScheme
from django.conf import settings
from simple_history.models import HistoricalRecords
from django_currentuser.db.models import CurrentUserField

class DAccount(models.Model):
    accountNumber = models.CharField(max_length=20, unique=True)
    balance = models.FloatField(default=0)
    amountWithdrawable = models.FloatField(default=0)
    freeWithdrawalBalance = models.FloatField(default=0)
    lockUpPeriod = models.IntegerField(default=settings.DACCOUNT_CONFIG["LOCK_OUT_PERIOD"])
    status = models.CharField(
        max_length=3,
        choices=settings.DACCOUNT_STATUS,
        default="LOCKED",
    )
    accountType = models.CharField(max_length=8, choices=settings.DACCOUNT_TYPE)
    dateCreated = models.DateTimeField(auto_now_add=True)
    createdBy = CurrentUserField()

    # RELATIONSHIPS
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="accounts")
    # branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    # creator = models.ForeignKey(Employee, on_delete=models.CASCADE)
    withdrawalScheme =  models.ForeignKey(
        WithdrawalScheme, on_delete=models.CASCADE, related_name="withdrawal_account", blank=True)
    # reportScheme = models.ForeignKey(ReportScheme, on_delete=models.CASCADE)

    def __str__(self):
        return ("%s",self.accountNumber)

    class Meta:
        ordering = ('accountNumber', )

      # HISTORY
    history = HistoricalRecords()
