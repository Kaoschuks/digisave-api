from django.db import models
from simple_history.models import HistoricalRecords
from .customer import Customer
from django.conf import settings


class RewardScheme(models.Model):
    name = models.CharField(max_length=500)
    rewardType = models.CharField(max_length=1, choices=settings.REWARD_TYPE)
    methodOfCalc = models.CharField(max_length=1, choices=settings.CALCULATION_METHOD)
  #Relations
  # scheme can contains many customers
    customers = models.ManyToManyField(Customer, related_name="rewards", blank=True)
    
  # HISTORY
    history = HistoricalRecords()

    def __str__(self):
        return  "%s (%s)" % (self.name, self.rewardType)

    