# Generated by Django 4.1.1 on 2022-10-06 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrmsusers',
            name='profile_image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
    ]
