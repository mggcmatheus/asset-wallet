import django
import os
import pandas as pd
from registration.models import Category, Ticker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


def run_category():
    print('Inserindo Categorias')
    Category(name='Ação').save()
    Category(name='Fundo Imobiliário').save()
    Category(name='ETF').save()
    Category(name='Indice').save()


def run():
    run_category()

    print('Inserindo ações')

    df = pd.read_csv("data/ações.txt", sep="	", header=0)

    for index, row in df.iterrows():
        print(f'Nome: {row[0]} - Ticker: {row[2]}')
        Ticker(
            name=row[0],
            code=row[2],
            category_id=1
        ).save()

    print('Inserindo FIIs')

    df = pd.read_csv("data/FIIs.txt", sep="	", header=0)

    for index, row in df.iterrows():
        print(f'Nome: {row[0]} - Ticker: {row[1]}')
        Ticker(
            name=row[0],
            code=row[1],
            category_id=2
        ).save()

    print('Inserindo ETFs')

    df = pd.read_csv("data/ETFs.txt", sep="	", header=0)

    for index, row in df.iterrows():
        print(f'Nome: {row[0]} - Ticker: {row[1]}')
        Ticker(
            name=row[0],
            code=row[1],
            category_id=3
        ).save()
