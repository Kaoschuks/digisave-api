from django.db import models
from api.models.daccount import DAccount
from django.conf import settings
from django_currentuser.middleware import get_current_user, get_current_authenticated_user
from simple_history.models import HistoricalRecords
from django_currentuser.db.models import CurrentUserField

class InterestScheme(models.Model):
    name = models.CharField(max_length=100)
    interestRate = models.FloatField(default=0) # rate is in percentage
    interestType = models.CharField(max_length=10, choices=settings.INTEREST_CALC_TYPE)
    frequency = models.CharField(max_length=10, choices=settings.INTEREST_FREQ)
    # HISTORY
    history = HistoricalRecords()


class SavingsScheme(models.Model):
    name = models.CharField(max_length=100)
    miniPrincipal = models.FloatField(
        default=settings.SAVINGSPLAN_CONFIG["MINIMUM_PRINCIPAL_DEFAULT"])
    minLumpsum = models.FloatField(
        default=settings.SAVINGSPLAN_CONFIG["MINIMUM_LUMPSUM"])
    allowedCurrencies = models.CharField(
        max_length=8,
        choices=settings.CURRENCIES,
        default=settings.SAVINGSPLAN_CONFIG["DEFAULT_CURRENCY"])
    savingsType = models.CharField(
        max_length=8,
        choices=settings.SAVINGS_TYPE,
        default=settings.SAVINGSPLAN_CONFIG["SAVINGS_TYPE_DEFAULT"])
    savingsFrequency = models.CharField(
        max_length=10,
        choices=settings.SAVINGS_FREQUENCY,
        default=settings.SAVINGSPLAN_CONFIG["SAVINGS_FREQUENCY_DEFAULT"])
    allowSwiftSave = models.BooleanField(
        default=settings.SAVINGSPLAN_CONFIG["ALLOW_SWIFT_SAVE_DEFAULT"])
    allowESave = models.BooleanField(
        default=settings.SAVINGSPLAN_CONFIG["ALLOW_ESAVE_DEFAULT"])
    allowMultiple = models.BooleanField(
        default=settings.SAVINGSPLAN_CONFIG["ALLOW_MULTIPLE_DEFAULT"])
    allowInterest = models.BooleanField(
        default=settings.SAVINGSPLAN_CONFIG["ALLOW_INTEREST_DEFAULT"])
    minimumInvestPeriod = models.IntegerField(
        default=settings.SAVINGSPLAN_CONFIG["MINIMUM_INVEST_PERIOD_DEFAULT"])
    minimumInvestPeriodUnit = models.CharField(
        max_length=8,
        choices=settings.MINIMUM_INVEST_PERIOD_UNIT,
        default=settings.
        SAVINGSPLAN_CONFIG["MINIMUM_INVEST_PERIOD_UNIT_DEFAULT"])
    createdBy = CurrentUserField()
    dateCreated = models.DateTimeField(auto_now_add=True)

    #RELATIONS
    interestScheme = models.ForeignKey(
        InterestScheme,
        on_delete=models.CASCADE,
        related_name="savings_scheme",
        blank=True,
        null=True
    )

    # HISTORY
    history = HistoricalRecords()
    def __str__(self):
            return self.name

    class Meta:
        ordering = ('pk', )



class SavingsPlan(models.Model):
    interestAccred = models.FloatField(default=0)
    lumpSum = models.FloatField(default=0)
    principal = models.FloatField(default=0)
    currency = models.CharField(
        max_length=8,
        choices=settings.CURRENCIES,
        default=settings.SAVINGSPLAN_CONFIG["DEFAULT_CURRENCY"])
    
    # RELATIONS
    account = models.OneToOneField(
        DAccount,
        on_delete=models.DO_NOTHING,
        related_name="plan_account"
    )
    
    savingsScheme = models.ForeignKey(SavingsScheme,
                                         on_delete=models.DO_NOTHING,
                                       related_name='scheme_plan')
    # HISTORY
    history = HistoricalRecords()

    def __str__(self):
            return self.savingsScheme.name

    class Meta:
        ordering = ('pk', )




class Aim(models.Model):
    name = models.CharField(max_length=50, blank=True,null=True)
    targetDate = models.DateField()
    calculatedAmount = models.FloatField()
    savingsFreq = models.CharField(
        max_length=1,
        choices=settings.SAVINGS_FREQUENCY,
        default=settings.SAVINGSPLAN_CONFIG["SAVINGS_FREQUENCY_DEFAULT"])

    # HISTORY
    history = HistoricalRecords()

    plan = models.OneToOneField(SavingsPlan,
                               on_delete=models.CASCADE,
                               related_name="aim")

    def __str__(self):
            return self.calculatedAmount

    class Meta:
        ordering = ('pk', )


class FundSource(models.Model):
    sourceType = models.CharField(
        max_length=3,
        choices=settings.FUND_SOURCE,
        default=settings.SAVINGSPLAN_CONFIG["FUND_SORUCE_DEFAULT"])
    info = models.CharField(max_length=200)
    
    plan = models.ForeignKey(SavingsPlan,
                                   related_name="plan_fundSource",
                                   on_delete=models.CASCADE)
    # HISTORY
    history = HistoricalRecords()

class ExternalBank(models.Model):
    accountName= models.CharField(max_length=100)
    accountNumber = models.CharField(max_length=20)
    accountType = models.CharField(max_length=100)
    allowedUSSDTrans = models.BooleanField()
    allowedPhoneTrans = models.BooleanField()
    bankName = models.CharField(max_length = 100)
    bankId = models.CharField(max_length = 100)
    # TODO: make secreteToken unique
    secreteToken=  models.CharField(max_length = 100)
    
    # RELATIONS
    fundSource = models.OneToOneField(
        FundSource,
        on_delete=models.CASCADE,
        blank = True,
        null=True,
        related_name = 'bank'
    )