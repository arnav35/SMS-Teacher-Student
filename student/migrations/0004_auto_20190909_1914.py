# Generated by Django 2.2.5 on 2019-09-09 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20190909_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exammodell',
            name='totalexammarks',
            field=models.CharField(choices=[(30, '30'), (70, '70')], max_length=50),
        ),
        migrations.AlterField(
            model_name='exammodell',
            name='typeexam',
            field=models.CharField(choices=[('Unit Test', 'Unit Test'), ('Final Test', 'Final Test')], max_length=50),
        ),
    ]