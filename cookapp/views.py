from django.shortcuts import render
from .models import Ingredient, Recipe

def home(request):
    if request.method == 'GET':
        print("one")
        ingredients = Ingredient.objects
        categories = Ingredient.objects.values_list('category', flat=True)
        categories = list(set(categories))
        code = [1, 2, 3, 4, 5,6]
        return render(request, 'home.html', {'ingredients' : ingredients, 'code' : code, 'categories' : categories})
    else :
        ingr = Ingredient.objects.values_list('name', flat=True)
        full_list = list(ingr)
        all = Recipe.objects
        print("all : ",all.all())
        print("3")
        choose = ["쌀밥", "삼겹살", "조밥", "요거트", "된장", "우유", "소면", "잡곡", "등심", "고추장"]
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
        print("end for")
        print(recipe)
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
        return render(request, 'list.html', {'all':all, 'recipes':recipe, 'add':add})