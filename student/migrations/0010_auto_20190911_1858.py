# Generated by Django 2.2.5 on 2019-09-11 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20190910_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentparent',
            name='parent_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.ParentModell'),
        ),
        migrations.AlterField(
            model_name='studentparent',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.StudentModell'),
        ),
        migrations.CreateModel(
            name='STmapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.ParentModell')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.StudentModell')),
            ],
        ),
    ]
