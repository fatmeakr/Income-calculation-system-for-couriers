# Generated by Django 3.1 on 2022-04-26 13:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransitCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, ''), (2, 'Rejected by courier'), (3, 'Towards the resturant'), (4, 'Received by courier')], default=0)),
                ('created_at', models.DateField()),
                ('business_owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transits_of_owner', to='user.bussinessowner')),
                ('cost', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='transit', to='income.transitcost')),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transits', to='user.courier')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rewards', to='user.courier')),
            ],
        ),
        migrations.CreateModel(
            name='PayrollDeduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(validators=[django.core.validators.MaxValueValidator(-1)])),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='payroll_deductions', to='user.courier')),
            ],
        ),
        migrations.CreateModel(
            name='CourierWeaklyIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.IntegerField(default=0)),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='waekly_incomes', to='user.courier')),
            ],
            options={
                'unique_together': {('date', 'courier')},
            },
        ),
        migrations.CreateModel(
            name='CourierIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.IntegerField(default=0)),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='incomes', to='user.courier')),
            ],
            options={
                'unique_together': {('date', 'courier')},
            },
        ),
    ]