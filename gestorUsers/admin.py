from django.contrib import admin
from django.apps import apps

# Register your models here.

models_app = apps.get_app_config('gestorUsers').get_models()


for model in models_app:
    admin.site.register(model)