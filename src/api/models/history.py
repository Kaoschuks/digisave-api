
# from django.db import models
# from api.models.daccount import *



# class DAccountHistory(models.Model):
#     ''' Keeps all the history of the account including credit, transfer, visits, debits and all activities'''
#     account = models.ForeignKey(DAccount, related_name='history', on_delete=models.CASCADE)


# class InterestHistory(models.Model):
#     message = models.CharField(max_length=500)
#     account = models.ForeignKey(DAccountHistory, related_name='interestHistory', on_delete=models.CASCADE)


# class TransferHistory(models.Model):
#     message = models.CharField(max_length=500)
#     account = models.ForeignKey(DAccountHistory, related_name='transferHistory', on_delete=models.CASCADE)


# class DebitHistory(models.Model):
#     message = models.CharField(max_length=500)
#     account = models.ForeignKey(DAccountHistory, related_name='debitHistory', on_delete=models.CASCADE)


# class CreditHistory(models.Model):
#     message = models.CharField(max_length=500)
#     account = models.ForeignKey(DAccountHistory, related_name='creditHistory',on_delete=models.CASCADE)
