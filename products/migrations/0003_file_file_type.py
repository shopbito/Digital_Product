# Generated by Django 4.2.1 on 2023-06-03 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_file_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'audio'), (2, 'video'), (3, 'pdf')], default=2, verbose_name='file_type'),
            preserve_default=False,
        ),
    ]
