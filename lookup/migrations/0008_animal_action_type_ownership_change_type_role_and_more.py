# Generated by Django 4.0.4 on 2022-07-17 08:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('movement', '0006_alter_animal_transfer_action_action_reason'),
        ('lookup', '0007_rename_trans_fee_type_transfer_fee_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='animal_action_type',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('active', models.BooleanField(default=False)),
                ('created_by', models.CharField(default=None, max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default=None, max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Animal Action Type',
                'verbose_name_plural': 'Animal Action Types',
            },
        ),
        migrations.CreateModel(
            name='ownership_change_type',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('active', models.BooleanField(default=False)),
                ('created_by', models.CharField(default=None, max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default=None, max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Ownership Change Type',
                'verbose_name_plural': 'Ownership Change Types',
            },
        ),
        migrations.CreateModel(
            name='role',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('active', models.BooleanField(default=False)),
                ('created_by', models.CharField(default=None, max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default=None, max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Roles',
                'verbose_name_plural': 'Role',
            },
        ),
        migrations.CreateModel(
            name='transit_category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('active', models.BooleanField(default=False)),
                ('created_by', models.CharField(default=None, max_length=100)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(default=None, max_length=100)),
                ('updated_timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Transfer Nature',
                'verbose_name_plural': 'Transfer Natures',
            },
        ),
        migrations.RenameModel(
            old_name='transfer_nature',
            new_name='movement_type',
        ),
        migrations.AlterModelOptions(
            name='movement_type',
            options={'verbose_name': 'Movement Type', 'verbose_name_plural': 'Movement Types'},
        ),
    ]
