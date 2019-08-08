from django.shortcuts import render
from .models import Ingredient, Recipe
from collections import defaultdict
from django.http import HttpResponse

from django.core.paginator import Paginator
import re

def home(request):
    if request.method == 'GET':
        ingredients = Ingredient.objects.all().order_by('category')
        data = defaultdict(list)
        for ingredient in ingredients:
            data[ingredient.category].append(ingredient)
        categories = Ingredient.objects.values_list('category', flat=True)
        categories = list(set(categories))
        categories = sorted(categories)
        response = render(request, 'cookapp/index.html', {'data' : dict(data)})
        response.set_cookie(key='recipe', value='select')
        return response

def cooklist(request):
    cookie_recipe = request.COOKIES.get('recipe')
    # print(cookie_recipe)
    ingr = Ingredient.objects.values_list('id', flat=True)
    full_list = list(ingr)
    all = Recipe.objects
    if(cookie_recipe == 'select'):
        data = request.GET['ingredients']
        print("try!!!")
        exist = 1

        print("데이터 : ",data)
        choose = data.split(',')
        choose = map(int, choose)
        print("choose : ",choose)
        sub = set(full_list) - set(choose)
        print(sub)
        print(len(sub))
        recipe = all
        print("레시피1 : ",recipe.all())
        if len(sub) != 0:
            print("if")
            recipe = recipe.exclude(ingredients__in=sub)
        else:
            print("else")
            recipe = recipe.all()
        print("레시피2 : ",recipe)
        add = []
        for r in all.all():
            sub = set(r.ingredients.values_list('id', flat=True)) - set(choose)
            if len(sub) == 1:
                add.append(r)

    else:
        data = request.GET.get('ingredients')
        print("except!!!")
        exist = 2
        p = re.compile('\d')
        cookie_recipe = request.COOKIES.get('recipe')
        cookie_recipe = list(map(int, p.findall(cookie_recipe)))

        print("쿠키레시피 : ",cookie_recipe)
        recipe = all.filter(id__in=cookie_recipe)
        add = []
    paginator = Paginator(recipe, 1)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    if exist == 1:
        print("exist 1")
        response = render(request, 'cookapp/list.html', {'recipes':recipe, 'add':add, 'posts':posts, 'ingredients':data})
        response.set_cookie(key='recipe',value=list(recipe.values_list('id', flat=True)))
        return response
    else:
        print("exist 2")
        return render(request, 'cookapp/list.html', {'recipes':recipe, 'add':add, 'posts':posts, 'ingredients':data})

    
def see(request,Rid):
    up = Recipe.objects.get(id=Rid)
    up.see = up.see + 1
    up.save()
    return HttpResponse('')

    
