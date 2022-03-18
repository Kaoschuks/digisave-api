from rest_framework.schemas import get_schema_view
from api.views import (agreement, customer, reward_scheme, daccount, withdrawal_scheme,
savings_plan, report_scheme, system)
from django.urls import path, include 
from rest_framework import routers


schema_view = get_schema_view(title='DigiSaver API V1')

router = routers.DefaultRouter()
router.register('agreements', agreement.AgreementViewSet)
router.register('branch', system.BranchViewSet)
router.register('employee', system.EmployeeViewSet)
router.register('withdrawal-scheme', withdrawal_scheme.WithdrawalSchemeViewSet)
router.register('report-scheme', report_scheme.ReportSchemeViewSet)
router.register('reward-scheme', reward_scheme.RewardSchemeViewSet)
router.register('interest-scheme', savings_plan.InterestSchemeViewSet)
router.register('savings-scheme', savings_plan.SavingsSchemeViewSet)
router.register('customer', customer.CustomerViewSet)
router.register('digisaver-account', daccount.DAccountViewSet)
# router.register('interest-history', view_set.InterestHistoryViewSet)
# router.register('transfer-history', view_set.TransferHistoryViewSet)
# router.register('debit-history', view_set.DebitHistoryViewSet)
# router.register('credit-history', view_set.CreditHistoryViewSet)
# router.register('account-history', view_set.DAccountHistoryViewSet)
# router.register('confirmations', view_set. DAccountTransConfirmationViewSet)
# router.register('verifications', view_set.DAccountTransVerificationViewSet)
# router.register('credits', view_set.CreditViewSet)
# router.register('debits', view_set.DebitViewSet)
# router.register('transfers', view_set.TransferViewSet)
# router.register('transactions', view_set.DTransactionViewSet)
# router.register('card-history', view_set.DCardHistoryViewSet)
# router.register('cards', view_set.DAccountCardViewSet)
router.register('savings-plans', savings_plan.SavingsPlanViewSet)
# router.register('fund-sources', view_set.FundSourceViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('schema/', schema_view)
]
