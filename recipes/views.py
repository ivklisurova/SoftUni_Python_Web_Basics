from django.shortcuts import render, redirect

# Create your views here.
from recipes.forms import RecipeForm, DeleteRecipeForm
from recipes.models import Recipe


def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)


def create(request):
    if request=='GET':
        form = RecipeForm()
        context = {
            'form': form
        }
        return render(request, 'create.html', context)
    else:
        form = RecipeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = {
                'form': form
            }
            return render(request, 'create.html', context)


def edit(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method=='GET':
        form = RecipeForm(instance=recipe)
        context = {
            'form': form
        }
        return render(request, 'edit.html', context)
    else:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = {
                'form': form
            }
            return render(request, 'edit.html', context)


def delete(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method=="GET":
        form = DeleteRecipeForm(instance=recipe)
        context = {
            'form': form
        }
        return render(request, 'delete.html', context)
    else:
        recipe.delete()
        return redirect('index')


def details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = [ingredient for ingredient in recipe.ingredients.split(',')]
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(request, 'details.html', context)
