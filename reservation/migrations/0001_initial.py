# Generated by Django 5.0.1 on 2024-01-23 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_id', models.CharField(max_length=32)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('FINISHED', 'Finished')], max_length=32)),
                ('card_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='card.carditem')),
            ],
        ),
    ]
