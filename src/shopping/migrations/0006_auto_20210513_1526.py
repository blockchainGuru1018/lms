# Generated by Django 2.2 on 2021-05-13 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_auto_20210513_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='bestellung',
            name='adresse',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='bestellung',
            name='email',
            field=models.CharField(blank=True, max_length=220),
        ),
        migrations.AddField(
            model_name='bestellung',
            name='land',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='bestellung',
            name='plz',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bestellung',
            name='stadt',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='bestellung',
            name='tax_nr',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bestellung',
            name='tel',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='bestellung',
            name='product',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='shopping.Product'),
        ),
    ]