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
    category_id: int


class TickerOut(Schema):
    id: str
    name: str
    code: str
    category_id: int
    is_active: bool
