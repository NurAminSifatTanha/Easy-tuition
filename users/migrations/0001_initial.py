# Generated by Django 3.1.6 on 2021-02-05 19:14

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_client', models.BooleanField(default=False)),
                ('is_tutor', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100, verbose_name='Full name')),
                ('bio', models.CharField(max_length=1000, verbose_name='Bio')),
                ('location', models.CharField(max_length=1000, verbose_name='Location')),
                ('gender', models.CharField(max_length=20, verbose_name='Gender')),
                ('title', models.CharField(max_length=1000, verbose_name='Overview title')),
                ('overview', models.TextField(verbose_name='Overview')),
                ('expertise', models.CharField(max_length=1000, verbose_name='Expertise')),
                ('profile_img', models.TextField(blank=True, verbose_name='Profile Image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='File Type')),
                ('file', models.TextField(verbose_name='File location')),
                ('verified', models.BooleanField(default=False, verbose_name='Verified')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(max_length=200, verbose_name='Institute')),
                ('department', models.CharField(max_length=200, verbose_name='Department')),
                ('degree', models.CharField(max_length=200, verbose_name='Degree')),
                ('result', models.CharField(max_length=200, verbose_name='Result')),
                ('from_year', models.DateField(verbose_name='From year')),
                ('to_year', models.DateField(verbose_name='To year')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
