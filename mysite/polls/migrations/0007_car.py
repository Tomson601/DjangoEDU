# Generated by Django 3.2.13 on 2022-04-15 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_coffee_tasty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('price', models.FloatField(max_length=100)),
                ('is_broken', models.BooleanField(default=False)),
            ],
        ),
    ]