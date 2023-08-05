# Generated by Django 4.2.3 on 2023-08-03 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100, null=True)),
                ('adress1', models.CharField(max_length=100, null=True)),
                ('adress2', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('website', models.CharField(max_length=100, null=True)),
                ('logo', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
