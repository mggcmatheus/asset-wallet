from ninja import Schema


class CategoryIn(Schema):
    name: str


class CategoryOut(Schema):
    id: int
    name: str
    is_active: bool


class TickerIn(Schema):
    name: str
    code: str
    price: float = 0.00
    category_id: int


class TickerUpdate(Schema):
    price = float


class TickerOut(Schema):
    id: str
    name: str
    code: str
    price: float
    category_id: int
    is_active: bool


class AssetWalletIn(Schema):
    name: str


class AssetWalletOut(Schema):
    id: str
    name: str
    is_active: bool
