from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id} | {self.name}'

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Ticker(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id} | {self.code} | {self.name}'

    class Meta:
        verbose_name = 'Ativo'
        verbose_name_plural = 'Ativos'


class AssetWallet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id} | {self.name}'

    class Meta:
        verbose_name = 'Carteira de ativos'
        verbose_name_plural = 'Carteiras de ativos'


class AssetsInWallet(models.Model):
    id = models.AutoField(primary_key=True)
    asset_wallet = models.ForeignKey(AssetWallet, on_delete=models.PROTECT)
    ticker = models.ForeignKey(Ticker, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Ativos na carteira'
        verbose_name_plural = 'Ativos na carteira'
