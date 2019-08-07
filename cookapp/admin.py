from django.contrib import admin

# Register your models here.
from .models import Ingredient, Recipe, Category

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Category)