# Generated by Django 3.2.13 on 2022-04-23 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_alter_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.CharField(max_length=50),
        ),
    ]
