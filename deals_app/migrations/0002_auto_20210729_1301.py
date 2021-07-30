# Generated by Django 3.2.5 on 2021-07-29 13:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('deals_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dealsmodel',
            options={'ordering': ('-created_at',), 'verbose_name': 'Deal', 'verbose_name_plural': 'Deals'},
        ),
        migrations.AddField(
            model_name='dealsmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]