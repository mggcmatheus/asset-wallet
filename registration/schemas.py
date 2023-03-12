from ninja import Schema, ModelSchema

from registration.models import *


class CategoryIn(Schema):
    name: str


class CategoryOut(ModelSchema):
    class Config:
        model = Category
        model_fields = ['id', 'name', 'is_active']


class TickerIn(Schema):
    name: str
    code: str
    price: float = 0.00
    category_id: int


class TickerUpdate(Schema):
    price = float


class TickerOut(ModelSchema):
    class Config:
        model = Ticker
        model_fields = ['id', 'name', 'code', 'price', 'category', 'is_active']


class AssetWalletIn(Schema):
    name: str


class AssetWalletOut(ModelSchema):
    class Config:
        model = Category
        model_fields = ['id', 'name', 'is_active']


class AssetsInWalletIn(Schema):
    asset_wallet: AssetWalletIn
    ticker: TickerIn
