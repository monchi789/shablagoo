# Generated by Django 4.1.3 on 2022-11-23 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('user', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('birthDate', models.DateField()),
                ('roleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.role')),
            ],
        ),
        migrations.CreateModel(
            name='EventPlanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='Events/images/')),
                ('ruc', models.CharField(max_length=11)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.user')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='Events/images/')),
                ('description', models.TextField()),
                ('dateEvent', models.DateField(blank=True)),
                ('price', models.CharField(max_length=10)),
                ('categoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.category')),
                ('eventPlannerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.eventplanner')),
            ],
        ),
    ]
