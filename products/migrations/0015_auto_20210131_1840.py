# Generated by Django 3.1.2 on 2021-01-31 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20210130_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(default='This is a text which describe category             and will be displayed in product page'),
        ),
    ]