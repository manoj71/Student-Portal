# Generated by Django 3.1.2 on 2020-12-07 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FEES',
            fields=[
                ('fee_id', models.AutoField(primary_key=True, serialize=False)),
                ('fee_sub', models.CharField(default='', max_length=50)),
                ('fee_desc', models.CharField(default='', max_length=500)),
                ('fee_document', models.FileField(blank=True, null=True, upload_to='fee/images')),
            ],
        ),
        migrations.CreateModel(
            name='FeeSem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typee', models.CharField(default='', max_length=5000)),
                ('pay_amount', models.CharField(default='', max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='FeeUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_id', models.CharField(default='', max_length=10000)),
                ('update_desc', models.CharField(default='', max_length=5000)),
                ('amount', models.CharField(default=0, max_length=10000000)),
                ('payment_status', models.CharField(default=0, max_length=10000000)),
                ('transaction_id', models.CharField(default=0, max_length=10000000)),
                ('name', models.CharField(default='', max_length=90)),
                ('email', models.CharField(default='', max_length=111)),
                ('address', models.CharField(default='', max_length=111)),
                ('roll_number', models.CharField(default='', max_length=111)),
                ('phone', models.CharField(default='', max_length=111)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=111)),
                ('address', models.CharField(max_length=111)),
                ('roll_number', models.CharField(max_length=111)),
                ('phone', models.CharField(default='', max_length=111)),
            ],
        ),
    ]
