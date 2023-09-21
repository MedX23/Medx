# Generated by Django 4.2.5 on 2023-09-16 21:42

import app.models.manager
from django.conf import settings
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
                ('phone', models.CharField(blank=True, default='', max_length=225, unique=True)),
                ('email', models.EmailField(blank=True, default='', max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, default='', max_length=225)),
                ('last_name', models.CharField(blank=True, default='', max_length=225)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('user_type', models.CharField(blank=True, max_length=255)),
                ('status', models.IntegerField(blank=True, default=0)),
                ('profile', models.FileField(blank=True, default=None, max_length=250, null=True, upload_to='profile/')),
                ('delete', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('object', app.models.manager.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_id', models.CharField(max_length=25, unique=True)),
                ('date', models.DateField()),
                ('slot_time', models.TimeField()),
                ('relation', models.CharField(choices=[('1', 'Self'), ('2', 'Father'), ('3', 'Mother'), ('4', 'Wife'), ('5', 'Husband'), ('6', 'Son'), ('7', 'Daughter'), ('8', 'Brother')], default='1', max_length=20)),
                ('region', models.CharField(blank=True, max_length=255)),
                ('doctor', models.CharField(blank=True, max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('appointment_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=25, unique=True)),
                ('problem', models.CharField(blank=True, max_length=255)),
                ('suggestion_test', models.CharField(blank=True, max_length=255)),
                ('medicine', models.CharField(blank=True, max_length=255)),
                ('patient_ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.appointment')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('payment_id', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('payment_mode', models.CharField(blank=True, max_length=50, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('payment_ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_id', models.CharField(max_length=50, unique=True)),
                ('position', models.CharField(blank=True, max_length=50)),
                ('qualification', models.CharField(blank=True, max_length=50)),
                ('pan', models.CharField(blank=True, max_length=50)),
                ('salary', models.IntegerField()),
                ('signature', models.FileField(default=None, max_length=250, null=True, upload_to='signature/')),
                ('dept_ref', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
