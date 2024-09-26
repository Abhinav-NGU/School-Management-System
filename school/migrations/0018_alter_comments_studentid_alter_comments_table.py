# Generated by Django 5.0.6 on 2024-09-20 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0017_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='studentid',
            field=models.ForeignKey(db_column='STUDENTID', on_delete=django.db.models.deletion.CASCADE, to='school.student'),
        ),
        migrations.AlterModelTable(
            name='comments',
            table='comments',
        ),
    ]
