# Generated by Django 4.2.7 on 2023-12-05 10:01

from django.db import migrations, models
import user.managers


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='myuser',
            managers=[
                ('objects', user.managers.MyUserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='activation_code',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
    ]
