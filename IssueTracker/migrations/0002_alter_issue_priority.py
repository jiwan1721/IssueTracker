# Generated by Django 4.0.4 on 2022-07-14 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IssueTracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('1', 'HIGH'), ('2', 'MEDIUM'), ('3', 'LOW')], default='low', max_length=30),
        ),
    ]
