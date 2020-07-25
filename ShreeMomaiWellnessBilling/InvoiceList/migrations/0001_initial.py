# Generated by Django 3.0.8 on 2020-07-25 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Product', '0001_initial'),
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('ProductCode', models.CharField(max_length=50)),
                ('UnitPrice', models.DecimalField(decimal_places=2, max_digits=9)),
                ('AmountTaken', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('Discount', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('Quantity', models.PositiveSmallIntegerField()),
                ('FinalAmount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('Fk_Order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Order.Order')),
                ('Fk_Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.Product')),
            ],
            options={
                'db_table': 'Product Order',
            },
        ),
    ]
