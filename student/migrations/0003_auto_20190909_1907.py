# Generated by Django 2.2.5 on 2019-09-09 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20190909_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='exammodell',
            name='totalexammarks',
            field=models.CharField(choices=[(20, '20'), (30, '30'), (70, '70')], default=999, max_length=50),
        ),
        migrations.AddField(
            model_name='exammodell',
            name='typeexam',
            field=models.CharField(choices=[('Class Test', 'Class Test'), ('Unit Test', 'Unit Test'), ('Final Test', 'Final Test')], default='null', max_length=50),
        ),
    ]
