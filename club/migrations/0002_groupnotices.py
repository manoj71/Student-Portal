# Generated by Django 3.1.2 on 2020-12-07 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groupnotices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_name', models.CharField(default='', max_length=50)),
                ('notice_category', models.CharField(default='', max_length=50)),
                ('notice_desc', models.CharField(default='', max_length=300)),
                ('notice_image', models.ImageField(blank=True, null=True, upload_to='clubs/images')),
                ('notice_date', models.DateTimeField(null=True)),
                ('notice_document', models.FileField(blank=True, null=True, upload_to='clubs/documents')),
            ],
        ),
    ]
