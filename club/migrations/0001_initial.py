# Generated by Django 3.1.2 on 2020-12-07 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(default='', max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=300)),
                ('detaileddesc', models.CharField(default='', max_length=300)),
                ('coordinator', models.CharField(default='', max_length=300)),
                ('image', models.ImageField(blank=True, null=True, upload_to='clubs/images')),
                ('pub_date', models.DateTimeField(null=True)),
                ('document', models.FileField(blank=True, null=True, upload_to='clubs/images')),
            ],
        ),
    ]
