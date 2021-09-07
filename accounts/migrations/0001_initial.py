# Generated by Django 3.2.7 on 2021-09-06 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=50)),
                ('full_name', models.CharField(max_length=50)),
                ('matric_number', models.CharField(max_length=50, unique=True)),
                ('session', models.CharField(blank=True, choices=[('', 'Select Year'), ('2020/2021', '2020/2021')], max_length=50)),
                ('College', models.CharField(blank=True, choices=[('', 'Select College'), ('COLLEGE OF SCIENCE', 'Science'), ('COLLEGE OF TECHNOLOGY', 'Technology')], max_length=50, null=True)),
                ('level', models.CharField(blank=True, choices=[('', 'Select Level'), ('300', '300'), ('400', '400')], max_length=50, null=True)),
                ('department', models.CharField(blank=True, choices=[('', 'Select Dept'), ('Chemistry', 'Chemistry'), ('Industrial Chemistry', 'Industrial Chemistry'), ('Physics', 'Physics'), ('Geophysics', 'Geophysics'), ('Geology', 'Geology'), ('Computer Science', 'Computer Science'), ('Mathematics', 'Mathematics'), ('Environmental Management Toxicology', 'Environmental Sci'), ('Petroleum Engineering', 'Petroleum Engr'), ('Chemical Engineering', 'Chemical Engr'), ('Electrical Electronics Engineering', 'Elect/Elect Engr'), ('Mechanical Engineering', 'Mechanical Engr'), ('Marine Engineering', 'Marine Engr')], max_length=50, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SiwesInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankName', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('accountNo', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('phoneNo', models.CharField(blank=True, max_length=50, null=True)),
                ('industryName', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('industryAddress', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('industrySupervisorname', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('industrySupervisorPhoneno', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]