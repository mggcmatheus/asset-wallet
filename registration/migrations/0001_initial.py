# Generated by Django 4.1.7 on 2023-03-12 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetWallet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Carteira de ativos',
                'verbose_name_plural': 'Carteiras de ativos',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='registration.category')),
            ],
            options={
                'verbose_name': 'Ativo',
                'verbose_name_plural': 'Ativos',
            },
        ),
        migrations.CreateModel(
            name='AssetsInWallet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('asset_wallet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='registration.assetwallet')),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='registration.ticker')),
            ],
            options={
                'verbose_name': 'Ativos na carteira',
                'verbose_name_plural': 'Ativos na carteira',
            },
        ),
    ]
