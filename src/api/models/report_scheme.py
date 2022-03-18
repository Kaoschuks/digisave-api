from django.db import models
from simple_history.models import HistoricalRecords
from django_currentuser.db.models import CurrentUserField
from django.conf import settings
from api.models.daccount import DAccount 

class ReportScheme(models.Model):
    name = models.CharField(max_length=100)
    show_accountId = models.BooleanField(default=settings.SAVINGSPLAN_CONFIG["REPORT_GEN_SHOW_ACCOUNT_ID"])
    show_accountType = models.BooleanField(default=settings.SAVINGSPLAN_CONFIG["REPORT_GEN_SHOW_ACCOUNT_TYPE"])
    show_planType = models.BooleanField(default=settings.SAVINGSPLAN_CONFIG["REPORT_GEN_SHOW_PLAN_TYPE"])
    show_accountHolder = models.BooleanField(default=settings.SAVINGSPLAN_CONFIG["REPORT_GEN_SHOW_ACCOUNT_HOLDER"])
    show_transactions = models.BooleanField(default=settings.SAVINGSPLAN_CONFIG["REPORT_GEN_SHOW_TRANSACTIONS"])
    show_currentBalance = models.BooleanField(default=settings.SAVINGSPLAN_CONFIG["REPORT_GEN_SHOW_BALANCE"])
    show_interestScheme = models.BooleanField(default=settings.SAVINGSPLAN_CONFIG["REPORT_GEN_SHOW_INTEREST_SCHEME"])
    show_aim = models.BooleanField(default=settings.SAVINGSPLAN_CONFIG["REPORT_GEN_SHOW_AIM"])
    genFrequency = models.CharField(max_length=10, choices=settings.REPORT_GENERATION_FREQUENCY,
    default=settings.SAVINGSPLAN_CONFIG["REPORT_GEN_FREQ_DEFAULT"])
    createdBy = CurrentUserField()
    dateCreated = models.DateTimeField(auto_now_add=True)

  # HISTORY 
    history = HistoricalRecords()

    accounts = models.ManyToManyField(DAccount, related_name="report_schemes", blank=True)
    

    def __str__(self):
            return ("%s (%s)", self.name, self.dateCreated)

    class Meta:
        ordering = ('dateCreated', 'pk','name' )

