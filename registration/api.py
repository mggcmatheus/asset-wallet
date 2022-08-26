from typing import List
from ninja import NinjaAPI
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Category, Ticker, AssetWallet
from .schemas import *

api = NinjaAPI()


# Category

@api.get("/categories", response=List[CategoryOut], tags=["category"])
def list_categories(request):
    qs = get_list_or_404(Category)
    return qs


@api.get("/categories/{category_id}", response=CategoryOut, tags=["category"])
def get_category(request, category_id: int):
    category = get_object_or_404(Category, id=category_id)
    return category


@api.post("/categories", tags=["category"])
def create_category(request, payload: CategoryIn):
    category = Category.objects.create(**payload.dict())
    return {"id": category.id}


@api.delete("/categories/{category_id}", tags=["category"])
def delete_category(request, category_id: int):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return {"success": True}


@api.put("/categories/{category_id}", tags=["category"])
def update_category(request, category_id: int, payload: CategoryIn):
    category = get_object_or_404(Category, id=category_id)
    for attr, value in payload.dict().items():
        setattr(category, attr, value)
    category.save()
    return {"success": True}


# Ticker

@api.get("/tickers", response=List[TickerOut], tags=["ticker"])
def list_tickers(request):
    qs = get_list_or_404(Ticker)
    return qs


@api.get("/tickers/category/{category_id}", response=List[TickerOut], tags=["ticker"])
def list_tickers_for_category(request, category_id: int):
    qs = Ticker.objects.filter(category_id=category_id)
    return qs


@api.get("/tickers/{code}", response=TickerOut, tags=["ticker"])
def get_ticker(request, code: str):
    ticker = get_object_or_404(Ticker, code=code.upper())
    return ticker


@api.post("/tickers", tags=["ticker"])
def create_ticker(request, payload: TickerIn):
    ticker = Ticker.objects.create(**payload.dict())
    return {"id": ticker.code.upper()}


@api.delete("/tickers/{code}", tags=["ticker"])
def delete_ticker(request, code: str):
    ticker = get_object_or_404(Ticker, code=code.upper())
    ticker.delete()
    return {"success": True}


@api.put("/tickers/{code}", tags=["ticker"])
def update_ticker(request, code: str, payload: TickerUpdate):
    ticker = get_object_or_404(Ticker, code=code.upper())
    for attr, value in payload.dict().items():
        setattr(ticker, attr, value)
    ticker.save()
    return {"success": True}


# AssetWallet

@api.get("/asset-wallet", response=List[AssetWalletOut], tags=["asset-wallet"])
def list_asset_wallets(request):
    qs = get_list_or_404(AssetWallet)
    return qs


@api.get("/asset-wallet/{wallet_id}", response=AssetWalletOut, tags=["asset-wallet"])
def get_asset_wallet(request, wallet_id: int):
    asset_wallet = get_object_or_404(AssetWallet, id=wallet_id)
    return asset_wallet


@api.post("/asset-wallet", tags=["asset-wallet"])
def create_asset_wallet(request, payload: AssetWalletIn):
    asset_wallet = AssetWallet.objects.create(**payload.dict())
    return {"id": asset_wallet.id}
