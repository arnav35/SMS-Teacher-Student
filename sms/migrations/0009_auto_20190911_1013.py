# Generated by Django 2.2.4 on 2019-09-11 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0008_attendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(),
        ),
    ]