# Generated by Django 2.2 on 2021-05-13 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_auto_20210513_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.FileField(blank=True, default='placholder_vYebXbG.png', null=True, upload_to='course/'),
        ),
    ]
