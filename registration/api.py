from ninja import Router
from ninja.pagination import paginate
from typing import List
from django.shortcuts import get_list_or_404, get_object_or_404

from .schemas import *

router = Router()


# Category

@router.get("/categories", response=List[CategoryOut], tags=["Categoria"], summary='Retorna todas as categorias')
def list_categories(request):
    """
    Retorna todas categorias
    :param request:
    :return: Lista contendo todas as categorias
    """
    qs = get_list_or_404(Category)
    return qs


@router.get("/categories/{category_id}", response=CategoryOut, tags=["Categoria"], summary='Retorna uma categoria')
def get_category(request, category_id: int):
    """
    To get an category please provide:
     - **category_id**
    """
    category = get_object_or_404(Category, id=category_id)
    return category


@router.post("/categories", tags=["Categoria"], summary='Cadastra uma categoria')
def create_category(request, payload: CategoryIn):
    """
    To create an category please provide:
     - **name**
    """
    category = Category.objects.create(**payload.dict())
    return {"id": category.id}


@router.delete("/categories/{category_id}", tags=["Categoria"], summary='Exclui uma categoria')
def delete_category(request, category_id: int):
    """
    To delete an category please provide:
     - **category_id**
    """
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return {"success": True}


@router.put("/categories/{category_id}", tags=["Categoria"], summary='Atualiza uma categoria')
def update_category(request, category_id: int, payload: CategoryIn):
    category = get_object_or_404(Category, id=category_id)
    for attr, value in payload.dict().items():
        setattr(category, attr, value)
    category.save()
    return {"success": True}


# Ticker

@router.get("/tickers", response=List[TickerOut], tags=["Ticker"], summary='Retorna todos os tickers')
@paginate()
def list_tickers(request):
    qs = get_list_or_404(Ticker)
    return qs


@router.get("/tickers/category/{category_id}", response=List[TickerOut], tags=["Ticker"],
            summary='Retorna todos os tickers filtrando por uma categoria')
def list_tickers_for_category(request, category_id: int):
    qs = Ticker.objects.filter(category_id=category_id)
    return qs


@router.get("/tickers/{code}", response=TickerOut, tags=["Ticker"], summary='Retorna um ticker especifico')
def get_ticker(request, code: str):
    ticker = get_object_or_404(Ticker, code=code.upper())
    return ticker


@router.post("/tickers", tags=["Ticker"], summary='Cadastra um ticker')
def create_ticker(request, payload: TickerIn):
    ticker = Ticker.objects.create(**payload.dict())
    return {"id": ticker.code.upper()}


@router.delete("/tickers/{code}", tags=["Ticker"], summary='Exclui um ticker')
def delete_ticker(request, code: str):
    ticker = get_object_or_404(Ticker, code=code.upper())
    ticker.delete()
    return {"success": True}


@router.put("/tickers/{code}", tags=["Ticker"], summary='Atualiza um ticker')
def update_ticker(request, code: str, payload: TickerUpdate):
    ticker = get_object_or_404(Ticker, code=code.upper())
    for attr, value in payload.dict().items():
        setattr(ticker, attr, value)
    ticker.save()
    return {"success": True}


# AssetWallet

@router.get("/asset-wallet", response=List[AssetWalletOut], tags=["Carteira de ativos"],
            summary='Retorna todas carteiras de ativos')
def list_asset_wallets(request):
    qs = get_list_or_404(AssetWallet)
    return qs


@router.get("/asset-wallet/{wallet_id}", response=AssetWalletOut, tags=["Carteira de ativos"],
            summary='Retorna uma carteira de ativos especifica')
def get_asset_wallet(request, wallet_id: int):
    asset_wallet = get_object_or_404(AssetWallet, id=wallet_id)
    return asset_wallet


@router.post("/asset-wallet", tags=["Carteira de ativos"], summary='Cria uma carteira de ativos')
def create_asset_wallet(request, payload: AssetWalletIn):
    asset_wallet = AssetWallet.objects.create(**payload.dict())
    return {"id": asset_wallet.id}


# AssetsInWallet

@router.post("/assets-in-wallet", tags=["Ativos na carteira"], summary='Insere um ticker em uma carteira')
def create_asset_in_wallet(request, payload: AssetsInWalletIn):
    asset_in_wallet = AssetsInWallet.objects.create(**payload.dict())
    return {"id": asset_in_wallet.id}
