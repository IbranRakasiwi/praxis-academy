# Generated by Django 2.2.12 on 2020-11-02 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0002_online_jumlah'),
    ]

    operations = [
        migrations.AlterField(
            model_name='online',
            name='jumlah',
            field=models.IntegerField(max_length=5, null=True),
        ),
    ]
