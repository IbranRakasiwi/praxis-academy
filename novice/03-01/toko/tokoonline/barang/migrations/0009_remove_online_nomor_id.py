# Generated by Django 2.2.12 on 2020-11-05 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0008_auto_20201102_0725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='online',
            name='nomor_id',
        ),
    ]
