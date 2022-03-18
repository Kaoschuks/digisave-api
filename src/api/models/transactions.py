# from django.db import models
# from  api.models.employee import *
# from  api.models.daccount import *

# class DTransaction(models.Model):
#     ''' Executing and monitoring all forms Transactions '''
#     initiator = models.ForeignKey(Employee, related_name='transaction', on_delete=models.CASCADE)


# class DAccountTransConfirmation(models.Model):
#     initiatedTime = models.DateField()
#     abortionTime = models.DateField()
#     isConfirmed = models.BooleanField()
#     transaction = models.OneToOneField(
#         DTransaction,
#         on_delete=models.CASCADE,
#         primary_key=True,
#         related_name = "confirmation"
#     )


# class DAccountTransVerification(models.Model):
#     message = models.CharField(max_length=500)
#     isVerified = models.BooleanField()
#     transaction = models.OneToOneField(
#         DTransaction,
#         on_delete=models.CASCADE,
#         primary_key=True,
#         related_name = "verification"
#     )


# class Credit(models.Model):
#     account = models.ForeignKey(DAccount, on_delete=models.CASCADE)
#     amount = models.FloatField()
#     transaction = models.OneToOneField(
#         DTransaction,
#         on_delete=models.CASCADE,
#         primary_key=True,
#         related_name = "credit",
#         blank = True,
#     )


# class Debit(models.Model):
#     account = models.ForeignKey(DAccount, on_delete=models.CASCADE)
#     amount = models.FloatField()
#     transaction = models.OneToOneField(
#         DTransaction,
#         on_delete=models.CASCADE,
#         primary_key=True,
#         related_name = "debit",
#         blank = True,
#     )


# class Transfer(models.Model):
#     creditAccount = models.ForeignKey(DAccount, on_delete=models.CASCADE, related_name="creditAccount")
#     debitAccount = models.ForeignKey(DAccount, on_delete=models.CASCADE, related_name="debitAccount")
#     amount = models.FloatField()
#     transaction = models.OneToOneField(
#         DTransaction,
#         on_delete=models.CASCADE,
#         primary_key=True,
#         related_name = "transfer",
#         blank = True,
#     )
