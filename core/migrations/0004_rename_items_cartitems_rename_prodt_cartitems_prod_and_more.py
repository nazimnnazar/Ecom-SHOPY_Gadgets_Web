# Generated by Django 4.1 on 2022-10-28 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_cartlist_items'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='items',
            new_name='CartItems',
        ),
        migrations.RenameField(
            model_name='cartitems',
            old_name='prodt',
            new_name='prod',
        ),
        migrations.RenameField(
            model_name='cartlist',
            old_name='dete_added',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='cartlist',
            name='cart_id',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
