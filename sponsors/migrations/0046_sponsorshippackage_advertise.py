# Generated by Django 2.0.13 on 2021-09-08 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0045_add_added_by_user_sponsorbenefit'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsorshippackage',
            name='advertise',
            field=models.BooleanField(default=False, help_text='If checked, this package will be advertised in the sponsosrhip application'),
        ),
    ]
