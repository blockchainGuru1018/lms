# Generated by Django 2.2 on 2021-04-26 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('update', models.DateTimeField(auto_now=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('img', models.FileField(blank=True, null=True, upload_to='course/')),
                ('description', models.TextField(blank=True, max_length=1024, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=120)),
                ('order', models.IntegerField()),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.Course')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
