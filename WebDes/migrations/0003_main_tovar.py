# Generated by Django 4.2.6 on 2023-12-12 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebDes', '0002_alter_zayavka_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='main_tovar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ploshad', models.CharField(max_length=255)),
                ('cost', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]