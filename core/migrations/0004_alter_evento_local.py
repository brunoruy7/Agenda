# Generated by Django 4.1.2 on 2022-10-14 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_evento_local'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='local',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
