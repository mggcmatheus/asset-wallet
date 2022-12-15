from ninja import NinjaAPI
from ninja.security import django_auth
from registration.api import router as registration_router

api = NinjaAPI(csrf=True)

api.add_router("/registration/", registration_router)