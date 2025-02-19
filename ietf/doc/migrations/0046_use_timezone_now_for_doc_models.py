# Generated by Django 2.2.28 on 2022-07-12 11:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0045_docstates_chatlogs_polls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deletedevent',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='docevent',
            name='time',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, help_text='When the event happened'),
        ),
        migrations.AlterField(
            model_name='dochistory',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='document',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='documentactionholder',
            name='time_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
