# Generated by Django 4.1.5 on 2023-02-03 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incubation_app', '0009_rename_name_mentor_first_name_mentor_bio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vision', models.TextField()),
                ('description', models.TextField()),
                ('about', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('objectivies', models.ManyToManyField(to='incubation_app.objective')),
                ('our_services', models.ManyToManyField(to='incubation_app.service')),
            ],
        ),
    ]