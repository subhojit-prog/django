# Generated by Django 2.2.9 on 2020-01-05 15:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('worklist', '0005_auto_20200104_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolistmodel',
            name='completed',
        ),
        migrations.AddField(
            model_name='todolistmodel',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='todolistmodel',
            name='title',
            field=models.CharField(max_length=3),
        ),
    ]