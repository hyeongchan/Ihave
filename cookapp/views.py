from django.shortcuts import render
from .models import Ingredient, Recipe

def home(request):
    if request.method == 'GET':
        ingredients = Ingredient.objects
        categories = Ingredient.objects.values_list('category', flat=True)
        categories = list(set(categories))
        return render(request, 'home.html', {'ingredients' : ingredients, 'categories' : categories})
    else :
        ingr = Ingredient.objects.values_list('name', flat=True)
        full_list = list(ingr)
        all = Recipe.objects
        choose = ["쌀밥", "삼겹살", "조밥", "요거트", "된장", "우유", "소면", "잡곡", "등심", "고추장"]
        sub = set(full_list) - set(choose)
        recipe = all
        for r in sub:
            recipe = recipe.exclude(ingredients__name = r)
        add = []
        for r in all.all():
            sub = set(r.ingredients.values_list('name', flat=True)) - set(choose)
            if len(sub) == 1:
                add.append(r)
        return render(request, 'list.html', {'all':all, 'recipes':recipe, 'add':add})
