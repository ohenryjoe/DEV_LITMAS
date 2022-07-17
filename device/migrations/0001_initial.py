# Generated by Django 3.2.6 on 2022-06-27 12:18

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lookup', '0001_initial'),
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_installed', models.DateField()),
                ('rfid', models.CharField(default='xx', max_length=40)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default=None, max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default=None, max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('animal_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='lookup.animal_type')),
                ('installed_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='person.person')),
                ('tag_status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='lookup.tag_status')),
            ],
        ),
        migrations.CreateModel(
            name='chip',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('manufacturer', models.CharField(default='', max_length=40)),
                ('frequency', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20)),
                ('iso_standard', models.CharField(default='ISO', max_length=40)),
                ('configurable', models.BooleanField()),
                ('uid_size', models.PositiveSmallIntegerField()),
                ('user_memory', models.PositiveSmallIntegerField()),
                ('write_protection', models.BooleanField()),
                ('access_key', models.CharField(blank=True, max_length=200, null=True)),
                ('write_endurance', models.PositiveSmallIntegerField()),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default=None, max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default=None, max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('tag', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='device.tag')),
            ],
        ),
    ]
