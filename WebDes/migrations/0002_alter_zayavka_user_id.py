# Generated by Django 4.2.6 on 2023-12-05 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WebDes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zayavka',
            name='User_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]