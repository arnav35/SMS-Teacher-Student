# Generated by Django 2.2.4 on 2019-09-09 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0006_exam'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Teacher')),
            ],
        ),
    ]
