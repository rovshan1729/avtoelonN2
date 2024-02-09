# Generated by Django 5.0.2 on 2024-02-09 13:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('option', '0006_auto_20240207_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='optionvalueextended',
            name='parent',
        ),
        migrations.CreateModel(
            name='OptionValueExtendedPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('position_value', models.CharField(max_length=256)),
                ('option_value_extend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values_extended_position', to='option.optionvalueextended')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
