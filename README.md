<h1 align="center">Asset Wallet</h1>

<p>🚀 An API, made in Python with Django-Ninja, using MySql and MongoDB databases.
 Applying asynchronous requests and high volume data caching techniques with REDIS.</p>

<p>Uma API, feita em Python com Django-Ninja, usando bancos de dados MySql e MongoDB.
 Aplicando solicitações assíncronas e técnicas de cache de dados de alto volume com REDIS.</p>

#

![Badge](https://img.shields.io/badge/license-MIT-gree?style=plastic&logo=license)
![Badge](https://img.shields.io/badge/Python-3.9.12-blue?style=plastic&logo=python)
![Badge](https://img.shields.io/badge/Django-4.1-blue?style=plastic&logo=django)

#

<p align="center">
 <a href="#Objetivo">Objetivo</a> •
 <a href="#Features">Features</a> • 
 <a href="#Pré-requisitos">Pré-requisitos</a> • 
 <a href="#Tecnologias">Tecnologias</a> • 
 <a href="#autor">Autor</a>
</p>

### Objetivo

<h3> 
	🚧  🚀 Em construção...  🚧
</h3>

### Features

- [x] Cadastro de categoria de ativo
-
    - [x] Visualização de Categoria de ativo
- [x] Cadastro de ativo
-
    - [x] Visualização de ativo
-
    - [x] Visualização de ativo por categoria
- [ ] Cadastro de preços do ativo
-
    - [ ] Diário
-
    - [ ] Desde o inicio de negociação
- [ ] Inteligência de sugestão de compra/venda
- [ ] Composição da carteira

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python](https://www.python.org). Além disto é bom ter um editor para trabalhar com o código
como [VSCode](https://code.visualstudio.com/).

### 🎲 Rodando o Back End (servidor)

```bash
# Clone este repositório
$ git clone <https://github.com/mggcmatheus/asset-wallet>

# Crie um ambiente virtual Python
$ python -m venv .venv

# Altere o arquivo .env-sample para .env e preencha com as informações corretas

# Ative o ambiente virtual
$ .venv/Script/activate

# Instale as dependências
$ pip install -r requirements2.txt

# Crie as Migrations do Django
$ python manage.py makemigrations

# Execute as migrates criadas
$ python manage.py migrate

# Rode o servidor
$ python manage.py runserver localhost:5000

# O servidor inciará na porta:5000 - acesse <http://localhost:5000/app/docs> 
# para abrir a documentação padrão OpenAPI da api.
```
 
### 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django Ninja](https://django-ninja.rest-framework.com/)
- [MongoDB](https://www.mongodb.com/pt-br)
- [MySql](https://www.mysql.com/)
- [Redis](https://redis.io)

### Autor
---
<a href="https://github.com/mggcmatheus">
 <sub><b>Matheus Clemente</b></sub></a> 🚀 


Feito com ❤️ por Matheus Clemente 👋🏽 Entre em contato!

[![Gmail Badge](https://img.shields.io/badge/-mggcmatheus@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:mggcmatheus@gmail.com)](mailto:mggcmatheus@gmail.com)
