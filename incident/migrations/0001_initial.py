# Generated by Django 3.2.6 on 2022-06-27 12:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animal', '0001_initial'),
        ('lookup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='incident',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField(default='description')),
                ('reporting_date', models.DateField()),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.CharField(default=None, max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default=None, max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
                ('animal', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='animal.animal')),
                ('incident_level', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='lookup.incident_level')),
                ('incident_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='lookup.incident_type')),
            ],
        ),
    ]
