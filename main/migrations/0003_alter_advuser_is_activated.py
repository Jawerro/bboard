# Generated by Django 4.0 on 2022-05-24 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_advuser_is_activated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advuser',
            name='is_activated',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Прошел активацию?'),
        ),
    ]
