# Generated by Django 4.0.4 on 2022-05-27 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IssueTracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='reporting_person',
        ),
    ]
