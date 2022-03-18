# Generated by Django 2.1.8 on 2019-05-09 16:58

import datetime
from django.db import migrations, models
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isSign', models.BooleanField(default=False)),
                ('signature', models.CharField(blank=True, max_length=300)),
                ('message', models.CharField(blank=True, max_length=500)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Aim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('targetDate', models.DateField()),
                ('calculatedAmount', models.FloatField()),
                ('savingsFreq', models.CharField(choices=[('DAILY', 'D'), ('WEEKLY', 'W'), ('MONTHLY', 'M')], default='DAILY', max_length=1)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('dateCreated', 'name', 'pk'),
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_phone', models.CharField(blank=True, max_length=20)),
                ('emergency_phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountNumber', models.CharField(max_length=20, unique=True)),
                ('balance', models.FloatField(default=0)),
                ('amountWithdrawable', models.FloatField(default=0)),
                ('freeWithdrawalBalance', models.FloatField(default=0)),
                ('lockUpPeriod', models.IntegerField(default=3650000)),
                ('status', models.CharField(choices=[('LOCKED', 'LCK'), ('INACTIVE', 'INA'), ('ACTIVE', 'ACT')], default='LOCKED', max_length=3)),
                ('accountType', models.CharField(choices=[('CORE_ACCOUNT', 'CORE'), ('SAVINGS_PLAN', 'SAVINGS')], max_length=8)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('accountNumber',),
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workId', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('MANAGER', 'MA'), ('ACCOUNTANT', 'AC'), ('SALES_PERSON', 'SP'), ('OTHER', 'OR')], default='OTHER', max_length=20)),
                ('employedDate', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('workId', 'pk'),
            },
        ),
        migrations.CreateModel(
            name='ExternalBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountName', models.CharField(max_length=100)),
                ('accountNumber', models.CharField(max_length=20)),
                ('accountType', models.CharField(max_length=100)),
                ('allowedUSSDTrans', models.BooleanField()),
                ('allowedPhoneTrans', models.BooleanField()),
                ('bankName', models.CharField(max_length=100)),
                ('bankId', models.CharField(max_length=100)),
                ('secreteToken', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FundSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourceType', models.CharField(choices=[('EXTERNAL_BANK', 'EB'), ('CARD_TRANSFER', 'CT'), ('PERSONAL_DEPOSIT', 'PD')], default='PERSONAL_DEPOSIT', max_length=3)),
                ('info', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalAgreement',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('isSign', models.BooleanField(default=False)),
                ('signature', models.CharField(blank=True, max_length=300)),
                ('message', models.CharField(blank=True, max_length=500)),
                ('date', models.DateField(default=datetime.date.today)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical agreement',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalAim',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('targetDate', models.DateField()),
                ('calculatedAmount', models.FloatField()),
                ('savingsFreq', models.CharField(choices=[('DAILY', 'D'), ('WEEKLY', 'W'), ('MONTHLY', 'M')], default='DAILY', max_length=1)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical aim',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalBranch',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('dateCreated', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical branch',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCustomer',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('home_phone', models.CharField(blank=True, max_length=20)),
                ('emergency_phone', models.CharField(max_length=20)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical customer',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDAccount',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('accountNumber', models.CharField(db_index=True, max_length=20)),
                ('balance', models.FloatField(default=0)),
                ('amountWithdrawable', models.FloatField(default=0)),
                ('freeWithdrawalBalance', models.FloatField(default=0)),
                ('lockUpPeriod', models.IntegerField(default=3650000)),
                ('status', models.CharField(choices=[('LOCKED', 'LCK'), ('INACTIVE', 'INA'), ('ACTIVE', 'ACT')], default='LOCKED', max_length=3)),
                ('accountType', models.CharField(choices=[('CORE_ACCOUNT', 'CORE'), ('SAVINGS_PLAN', 'SAVINGS')], max_length=8)),
                ('dateCreated', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical d account',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalEmployee',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('workId', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('MANAGER', 'MA'), ('ACCOUNTANT', 'AC'), ('SALES_PERSON', 'SP'), ('OTHER', 'OR')], default='OTHER', max_length=20)),
                ('employedDate', models.DateField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical employee',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalFundSource',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('sourceType', models.CharField(choices=[('EXTERNAL_BANK', 'EB'), ('CARD_TRANSFER', 'CT'), ('PERSONAL_DEPOSIT', 'PD')], default='PERSONAL_DEPOSIT', max_length=3)),
                ('info', models.CharField(max_length=200)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical fund source',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalInterestScheme',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('interestRate', models.FloatField(default=0)),
                ('interestType', models.CharField(choices=[('SIMPLE_INTEREST', 'SI'), ('COMPOUND_INTEREST', 'CI')], max_length=10)),
                ('frequency', models.CharField(choices=[('DAILY', 'DA'), ('WEEKLY', 'WE'), ('MONTHLY', 'MON'), ('YEARLY', 'YE')], max_length=10)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical interest scheme',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalReportScheme',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('show_accountId', models.BooleanField(default=False)),
                ('show_accountType', models.BooleanField(default=False)),
                ('show_planType', models.BooleanField(default=False)),
                ('show_accountHolder', models.BooleanField(default=False)),
                ('show_transactions', models.BooleanField(default=False)),
                ('show_currentBalance', models.BooleanField(default=False)),
                ('show_interestScheme', models.BooleanField(default=False)),
                ('show_aim', models.BooleanField(default=False)),
                ('genFrequency', models.CharField(choices=[('DAILY', 'DA'), ('WEEKLY', 'WE'), ('MONTHLY', 'MON'), ('QUATERLY', 'QUA'), ('SEMIANUM', 'SEM'), ('YEARLY', 'YEA')], default='MONTHLY', max_length=10)),
                ('dateCreated', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical report scheme',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalRewardScheme',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('rewardType', models.CharField(choices=[('REFERRALS', 'REF'), ('BONUS', 'BON')], max_length=1)),
                ('methodOfCalc', models.CharField(choices=[('NOTAPPLY', 'NO'), ('ASSIGN', 'AS'), ('REFERAL', 'RE')], max_length=1)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical reward scheme',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSavingsPlan',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('interestAccred', models.FloatField(default=0)),
                ('lumpSum', models.FloatField(default=0)),
                ('principal', models.FloatField(default=0)),
                ('currency', models.CharField(choices=[('DOLAR', 'DO'), ('NAIRA', 'NA')], default='NAIRA', max_length=8)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical savings plan',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSavingsScheme',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('miniPrincipal', models.FloatField(default=1000.0)),
                ('minLumpsum', models.FloatField(default=1000.0)),
                ('allowedCurrencies', models.CharField(choices=[('DOLAR', 'DO'), ('NAIRA', 'NA')], default='NAIRA', max_length=8)),
                ('savingsType', models.CharField(choices=[('SMART_SAVE', 'SMART'), ('SELECT_SAVE', 'SELECT'), ('SECURE_SAVE', 'SECURE'), ('KID_SAVE', 'KID')], default='SMART_SAVE', max_length=8)),
                ('savingsFrequency', models.CharField(choices=[('DAILY', 'D'), ('WEEKLY', 'W'), ('MONTHLY', 'M')], default='DAILY', max_length=10)),
                ('allowSwiftSave', models.BooleanField(default=False)),
                ('allowESave', models.BooleanField(default=False)),
                ('allowMultiple', models.BooleanField(default=False)),
                ('allowInterest', models.BooleanField(default=False)),
                ('minimumInvestPeriod', models.IntegerField(default=6)),
                ('minimumInvestPeriodUnit', models.CharField(choices=[('YEARS', 'Y'), ('MONTHS', 'M'), ('WEEKS', 'W')], default='MONTHS', max_length=8)),
                ('dateCreated', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical savings scheme',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalWithdrawalScheme',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('totalAllowedWithdrawals', models.IntegerField()),
                ('allowedDates', models.CharField(max_length=500)),
                ('penaltyRate', models.FloatField()),
                ('maxAmountAllowed', models.FloatField()),
                ('emergencyAllowedWithdrawals', models.IntegerField()),
                ('withdrawalInterval', models.IntegerField(default=1)),
                ('withdrawalIntervalUnit', models.CharField(choices=[('MONTHS', 'M'), ('WEEKS', 'W'), ('DAYS', 'D')], default='MONTHS', max_length=10)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical withdrawal scheme',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='InterestScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('interestRate', models.FloatField(default=0)),
                ('interestType', models.CharField(choices=[('SIMPLE_INTEREST', 'SI'), ('COMPOUND_INTEREST', 'CI')], max_length=10)),
                ('frequency', models.CharField(choices=[('DAILY', 'DA'), ('WEEKLY', 'WE'), ('MONTHLY', 'MON'), ('YEARLY', 'YE')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ReportScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('show_accountId', models.BooleanField(default=False)),
                ('show_accountType', models.BooleanField(default=False)),
                ('show_planType', models.BooleanField(default=False)),
                ('show_accountHolder', models.BooleanField(default=False)),
                ('show_transactions', models.BooleanField(default=False)),
                ('show_currentBalance', models.BooleanField(default=False)),
                ('show_interestScheme', models.BooleanField(default=False)),
                ('show_aim', models.BooleanField(default=False)),
                ('genFrequency', models.CharField(choices=[('DAILY', 'DA'), ('WEEKLY', 'WE'), ('MONTHLY', 'MON'), ('QUATERLY', 'QUA'), ('SEMIANUM', 'SEM'), ('YEARLY', 'YEA')], default='MONTHLY', max_length=10)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('dateCreated', 'pk', 'name'),
            },
        ),
        migrations.CreateModel(
            name='RewardScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('rewardType', models.CharField(choices=[('REFERRALS', 'REF'), ('BONUS', 'BON')], max_length=1)),
                ('methodOfCalc', models.CharField(choices=[('NOTAPPLY', 'NO'), ('ASSIGN', 'AS'), ('REFERAL', 'RE')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='SavingsPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interestAccred', models.FloatField(default=0)),
                ('lumpSum', models.FloatField(default=0)),
                ('principal', models.FloatField(default=0)),
                ('currency', models.CharField(choices=[('DOLAR', 'DO'), ('NAIRA', 'NA')], default='NAIRA', max_length=8)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='SavingsScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('miniPrincipal', models.FloatField(default=1000.0)),
                ('minLumpsum', models.FloatField(default=1000.0)),
                ('allowedCurrencies', models.CharField(choices=[('DOLAR', 'DO'), ('NAIRA', 'NA')], default='NAIRA', max_length=8)),
                ('savingsType', models.CharField(choices=[('SMART_SAVE', 'SMART'), ('SELECT_SAVE', 'SELECT'), ('SECURE_SAVE', 'SECURE'), ('KID_SAVE', 'KID')], default='SMART_SAVE', max_length=8)),
                ('savingsFrequency', models.CharField(choices=[('DAILY', 'D'), ('WEEKLY', 'W'), ('MONTHLY', 'M')], default='DAILY', max_length=10)),
                ('allowSwiftSave', models.BooleanField(default=False)),
                ('allowESave', models.BooleanField(default=False)),
                ('allowMultiple', models.BooleanField(default=False)),
                ('allowInterest', models.BooleanField(default=False)),
                ('minimumInvestPeriod', models.IntegerField(default=6)),
                ('minimumInvestPeriodUnit', models.CharField(choices=[('YEARS', 'Y'), ('MONTHS', 'M'), ('WEEKS', 'W')], default='MONTHS', max_length=8)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='WithdrawalScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('totalAllowedWithdrawals', models.IntegerField()),
                ('allowedDates', models.CharField(max_length=500)),
                ('penaltyRate', models.FloatField()),
                ('maxAmountAllowed', models.FloatField()),
                ('emergencyAllowedWithdrawals', models.IntegerField()),
                ('withdrawalInterval', models.IntegerField(default=1)),
                ('withdrawalIntervalUnit', models.CharField(choices=[('MONTHS', 'M'), ('WEEKS', 'W'), ('DAYS', 'D')], default='MONTHS', max_length=10)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
