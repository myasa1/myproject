# Generated by Django 3.1.1 on 2020-09-19 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProdName', models.CharField(max_length=50)),
                ('ProdDesc', models.TextField(max_length=1000)),
                ('ProdPrice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ProdCost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ProdCreated', models.DateTimeField(auto_now=True)),
                ('ProdImage', models.ImageField(blank=True, null=True, upload_to='product/')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProdImage', models.ImageField(blank=True, null=True, upload_to='product/')),
                ('PrdProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
