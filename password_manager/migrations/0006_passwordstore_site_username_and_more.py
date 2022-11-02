# Generated by Django 4.1.2 on 2022-11-02 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('password_manager', '0005_rename_site_name_passwordstore_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='passwordstore',
            name='site_username',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='passwordstore',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='passwordstore',
            name='site_url',
            field=models.URLField(blank=True, max_length=520),
        ),
    ]
