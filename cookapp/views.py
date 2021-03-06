from django.shortcuts import render
from .models import Ingredient, Recipe
from collections import defaultdict
from django.http import HttpResponse

from django.core.paginator import Paginator
import re
from django.contrib import messages

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
    ingr = Ingredient.objects.values_list('id', flat=True)
    full_list = list(ingr)
    all = Recipe.objects
    if(cookie_recipe == 'select'):
        exist = 1
        data = request.GET['ingredients']
        if not data :
            data = ""
            recipe = Recipe.objects.none()
        else:
            choose = data.split(',')
            choose = map(int, choose)
            sub = set(full_list) - set(choose)
            recipe = all
            if len(sub) != 0:
                recipe = recipe.exclude(ingredients__in=sub)
            else:
                recipe = recipe.all()
    else:
        data = request.GET.get('ingredients')
        exist = 2
        p = re.compile('\d')
        cookie_recipe = request.COOKIES.get('recipe')
        cookie_recipe = list(map(int, p.findall(cookie_recipe)))
        recipe = all.filter(id__in=cookie_recipe)
    paginator = Paginator(recipe, 1)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    if data == "" :
        ingredients = Ingredient.objects.none()
    else:
        ingredients = Ingredient.objects.filter(id__in=map(int,data.split(',')))
    if exist == 1:
        response = render(request, 'cookapp/list.html', {'recipes':recipe, 'posts':posts, 'ingredients':data, 'ingredients_obj':ingredients})
        response.set_cookie(key='recipe',value=list(recipe.values_list('id', flat=True)))
        return response
    else:
        return render(request, 'cookapp/list.html', {'recipes':recipe, 'posts':posts, 'ingredients':data, 'ingredients_obj':ingredients})

    
def see(request,Rid):
    up = Recipe.objects.get(id=Rid)
    up.see = up.see + 1
    up.save()
    return HttpResponse('')

def add(request):
    data = request.GET['ingredients']
    if not data:
        data = ""
        choose = []
    else :
        choose = data.split(',')
        choose = list(map(int, choose))
    print("choose : ",choose)
    recipe = []
    for r in Recipe.objects.all():
        sub = set(r.ingredients.values_list('id', flat=True)) - set(choose)
        if len(sub) == 1:
            recipe.append(r)
    if data == "" :
        ingredients = Ingredient.objects.none()
    else :
        ingredients = Ingredient.objects.filter(id__in=map(int,data.split(',')))
    print("recipe : ",recipe)
    paginator = Paginator(recipe, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'cookapp/list.html', {'recipe':recipe, 'posts':posts, 'ingredients':data, 'ingredients_obj':ingredients})

def about(request):
    return render(request, 'cookapp/about.html')