# Generated by Django 4.1.1 on 2022-09-27 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_address_street2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
