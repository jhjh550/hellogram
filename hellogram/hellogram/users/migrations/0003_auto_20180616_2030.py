# Generated by Django 2.0.6 on 2018-06-16 11:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180616_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follower',
            field=models.ManyToManyField(related_name='_user_follower_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(related_name='_user_following_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
