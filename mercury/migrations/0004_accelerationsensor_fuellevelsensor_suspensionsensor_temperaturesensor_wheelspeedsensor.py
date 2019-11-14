# Generated by Django 2.2.6 on 2019-11-13 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercury', '0003_auto_20191104_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccelerationSensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('acceleration_x', models.FloatField(default=0)),
                ('acceleration_y', models.FloatField(default=0)),
                ('acceleration_z', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FuelLevelSensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('current_fuel_level', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SuspensionSensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('suspension_fr', models.FloatField(default=0)),
                ('suspension_fl', models.FloatField(default=0)),
                ('suspension_br', models.FloatField(default=0)),
                ('suspension_bl', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TemperatureSensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('temperature', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WheelSpeedSensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('wheel_speed_fr', models.FloatField(default=0)),
                ('wheel_speed_fl', models.FloatField(default=0)),
                ('wheel_speed_br', models.FloatField(default=0)),
                ('wheel_speed_bl', models.FloatField(default=0)),
            ],
        ),
    ]
