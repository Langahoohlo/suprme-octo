# Generated by Django 4.2.3 on 2023-09-21 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0008_alter_item_city_alter_item_phone_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='city',
            field=models.CharField(choices=[('Maseru', 'Maseru'), ('Berea', 'Berea'), ('Hlotse', 'Hlotse'), ('Mafeteng', 'Mafeteng'), ('Mokhotlong', 'Mokhotlong'), ('Butha-Bothe', 'Butha-Bothe')], max_length=50),
        ),
        migrations.AlterField(
            model_name='item',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
