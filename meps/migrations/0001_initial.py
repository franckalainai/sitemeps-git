# Generated by Django 3.2.14 on 2022-09-15 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ministere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=100)),
                ('resume', models.CharField(max_length=1000)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='media/')),
            ],
        ),
    ]
