# Generated by Django 4.1.7 on 2023-02-26 20:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('incubation_app', '0011_notice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='updates',
        ),
        migrations.AddField(
            model_name='notice',
            name='update',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
