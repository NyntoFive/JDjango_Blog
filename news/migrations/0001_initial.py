# Generated by Django 3.0.1 on 2020-01-03 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Headline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.URLField(blank=True, null=True)),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='KnifeKit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('sku', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('img_urls', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('keys', models.CharField(max_length=200)),
                ('mdesc', models.CharField(max_length=200)),
            ],
        ),
    ]
