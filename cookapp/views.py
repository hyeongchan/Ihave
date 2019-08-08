from django.shortcuts import render
from .models import Ingredient, Recipe
from collections import defaultdict
from django.http import HttpResponse

def home(request):
    if request.method == 'GET':
        ingredients = Ingredient.objects.all().order_by('category')
        data = defaultdict(list)
        for ingredient in ingredients:
            data[ingredient.category].append(ingredient)
        categories = Ingredient.objects.values_list('category', flat=True)
        categories = list(set(categories))
        categories = sorted(categories)
        return render(request, 'cookapp/index.html', {'data' : dict(data)})

def cooklist(request):
    # print(request.META)
    cookie_recipe = request.COOKIES.get('recipe')
    print(RRRRRR)
    ingr = Ingredient.objects.values_list('id', flat=True)
    full_list = list(ingr)
    all = Recipe.objects
    choose = request.GET['ingredients'].split(',')
    choose = map(int,choose)
    print("선택 : ",choose)

    sub = set(full_list) - set(choose)
    recipe = all
    if len(sub) != 0:
        recipe = recipe.exclude(ingredients__in=sub)
    else:
        recipe = recipe.all()
    add = []
    for r in all.all():
        sub = set(r.ingredients.values_list('id', flat=True)) - set(choose)
        if len(sub) == 1:
            add.append(r)

    # add = all.none()
    # for r in all.all():
    #     sub = set(r.ingredients.values_list('id', flat=True)) - set(choose)
    #     print("sub :",sub)
    #     print("length : ",len(sub))
    #     if len(sub) == 1:
    #         add |= r
    #         print("추가 : ",add)
    
    # sub = set(full_list) - set(choose)
    # if len(sub) != 0:
    #     recipe = add.exclude(ingredients__in=sub)
    # else:
    #     recipe = recipe.all()
    response = render(request, 'cookapp/list.html', {'recipes':recipe, 'add':add})
    response.set_cookie(key='recipe',value=list(recipe.values_list('id',flat=True)))
    return response

    
def see(request,Rid):
    up = Recipe.objects.get(id=Rid)
    up.see = up.see + 1
    up.save()
    return HttpResponse('')

    
