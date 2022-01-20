# Generated by Django 3.1.6 on 2021-02-10 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_radius', '0020_added_optional_registration_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationradiussettings',
            name='registration_enabled',
            field=models.BooleanField(
                blank=True,
                default=True,
                help_text='Whether the registration API endpoint should be enabled or '
                'not',
                null=True,
            ),
        ),
    ]
