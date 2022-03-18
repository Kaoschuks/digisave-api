from django.contrib import admin
from api.models import (agreement, customer, daccount, report_scheme,
reward_scheme, savings_plan, system, transactions, withdrawal_scheme)
# Register your models here.
admin.site.register(agreement.Agreement)
admin.site.register(customer.Customer)
admin.site.register(daccount.DAccount)
admin.site.register(report_scheme.ReportScheme)
admin.site.register(reward_scheme.RewardScheme)
admin.site.register(savings_plan.InterestScheme)
admin.site.register(savings_plan.SavingsScheme)
admin.site.register(savings_plan.SavingsPlan)
admin.site.register(savings_plan.Aim)
admin.site.register(savings_plan.FundSource)
admin.site.register(savings_plan.ExternalBank)
admin.site.register(system.Branch)
admin.site.register(system.Employee)
admin.site.register(withdrawal_scheme.WithdrawalScheme)