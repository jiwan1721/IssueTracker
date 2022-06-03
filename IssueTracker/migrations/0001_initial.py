# Generated by Django 3.2.10 on 2022-06-03 02:19

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=20, unique=True)),
                ('company', models.CharField(max_length=120)),
                ('mobile_number', models.CharField(max_length=10, unique=True)),
                ('level', models.CharField(choices=[(0, 'level zero'), (1, 'Level one'), (2, 'Level two'), (3, 'Level three')], default=0, max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('level', models.CharField(choices=[(0, 'level zero'), (1, 'Level one'), (2, 'Level two'), (3, 'Level three')], default=1, max_length=20)),
                ('status_code', models.CharField(choices=[('404', '404'), ('304', '404'), ('500', '500'), ('501', '500'), ('502', '502'), ('other', 'Other')], default='other', max_length=30)),
                ('module', models.CharField(choices=[('attendence', 'Attendence'), ('payroll', 'PayRoll'), ('leave', 'Leave'), ('calender', 'Calender'), ('worklog', 'Worklog'), ('other', 'Other')], default='other', max_length=30)),
                ('priority', models.CharField(choices=[('high', 'HIGH'), ('medium', 'MEDIUM'), ('low', 'LOW')], default='low', max_length=30)),
                ('company_name', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('solved', 'Solved'), ('forward', 'Forward')], default='pending', max_length=20)),
                ('upload_file', models.FileField(blank=True, max_length=250, upload_to='issue_file/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view_Issue', 'can see issue'), ('report_issue', 'user can report issue'), ('forward_issue', 'user can forwad isuue to senior level'), ('solve_Issue', 'can solve Issue')),
            },
        ),
    ]
