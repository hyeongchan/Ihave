from django.shortcuts import render
from .models import Ingredient, Recipe
from collections import defaultdict

def home(request):
    if request.method == 'GET':
        ingredients = Ingredient.objects.all().order_by('category')
        data = defaultdict(list)
        for ingredient in ingredients:
            data[ingredient.category].append(ingredient.name)
        categories = Ingredient.objects.values_list('category', flat=True)
        categories = list(set(categories))
        categories = sorted(categories)
        return render(request, 'cookapp/index.html', {'data' : dict(data)})
    else :
        ingr = Ingredient.objects.values_list('name', flat=True)
        full_list = list(ingr)
        all = Recipe.objects
        choose = request.POST['ingredients'].split(',')
        sub = set(full_list) - set(choose)
        recipe = all
        if len(sub) != 0:
            for r in sub:
                recipe = recipe.exclude(ingredients__name = r)
        else:
            recipe = recipe.all()
        add = []
        for r in all.all():
            sub = set(r.ingredients.values_list('name', flat=True)) - set(choose)
            if len(sub) == 1:
                add.append(r)
        return render(request, 'cookapp/list.html', {'recipes':recipe, 'add':add})
