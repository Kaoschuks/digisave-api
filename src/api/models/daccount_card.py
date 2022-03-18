from django.db import models
from api.models.daccount import *
from api.models.transactions import *
from api.models.customer import *

class DCardHistory(models.Model):
    message = models.CharField(max_length=500)
    dateCreated = models.DateField()

class DAccountCard(models.Model):
    ''' Define the cards that should be used for transactions, Multiple cards permitted'''
    CARD_TYPE = (("DIAMOND", "DI"), ("GOLD", "GO"), ("BRONZE", "BR"))
    cardType = models.CharField(max_length=3, choices=CARD_TYPE)
    lastUsed = models.DateField()

     # RELATIONS
    history = models.ForeignKey(DCardHistory,
    related_name="card",  on_delete=models.CASCADE)

    accountHolder = models.ForeignKey(Customer,
    related_name="card",  on_delete=models.CASCADE)

    linkedAccount = models.OneToOneField(
        DAccount,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name = "account"
    )

    transaction = models.ForeignKey(DTransaction,
    related_name="card", on_delete=models.CASCADE)