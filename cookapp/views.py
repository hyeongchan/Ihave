from django.shortcuts import render
from .models import Ingredient, Recipe
from collections import defaultdict

def home(request):
    if request.method == 'GET':
        ingredients = Ingredient.objects.all().order_by('category')
        data = defaultdict(list)
        for ingredient in ingredients:
            data[ingredient.category].append(ingredient.name)
        print(data)
        categories = Ingredient.objects.values_list('category', flat=True)
        categories = list(set(categories))
        categories = sorted(categories)
        print(categories)
        return render(request, 'cookapp/index.html', {'data' : dict(data)})
    else :
        print("in")
        ingr = Ingredient.objects.values_list('name', flat=True)
        print("1")
        full_list = list(ingr)
        print("2")
        all = Recipe.objects
        print("all : ",all.all())
        print("3")
        # choose = ["쌀밥", "삼겹살", "조밥", "요거트", "된장", "우유", "소면", "잡곡", "등심", "고추장"]
        choose = request.POST['ingredients'].split(',')
        print(choose)
        print("4")
        sub = set(full_list) - set(choose)
        print("5")
        recipe = all
        print("recipe : ",recipe)
        print("sub : ",sub)
        print("6")
        for r in sub:
            print("r : ",r)
            recipe = recipe.exclude(ingredients__name = r)
            print("in loop, recipe : ",recipe)
        print("end for")
        # print(recipe)
        print("7")
        add = []
        for r in all.all():
            print("loop")
            sub = set(r.ingredients.values_list('name', flat=True)) - set(choose)
            print("sub : ",sub)
            if len(sub) == 1:
                add.append(r)
            print("add : ",add)
        print("8")
        return render(request, 'cookapp/list.html', {'all':all.all(), 'recipes':recipe, 'add':add})
