# Generated by Django 4.2.6 on 2023-11-03 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('tmef', models.TextField(null=True)),
                ('wf', models.TextField(null=True)),
                ('tmn', models.IntegerField(default=0)),
                ('tmx', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('point', models.FloatField(default=0.0)),
                ('reserve', models.FloatField(default=0.0)),
            ],
        ),
    ]