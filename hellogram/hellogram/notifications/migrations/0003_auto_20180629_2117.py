# Generated by Django 2.0.6 on 2018-06-29 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20180629_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='images.Image'),
        ),
    ]
