# Generated by Django 4.1.5 on 2023-11-15 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Front', '0003_alter_payments_amount_alter_points_points_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='points',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='points',
            name='redeemed',
            field=models.IntegerField(default=0),
        ),
    ]
