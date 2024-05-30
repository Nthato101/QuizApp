# Generated by Django 4.2.7 on 2024-05-30 12:07

from django.db import migrations, models
import quiz.models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_player_last_login_player_password_player_user'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', quiz.models.CustomUserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='has_played',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='score',
        ),
        migrations.AddField(
            model_name='player',
            name='first_name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='last_name',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
