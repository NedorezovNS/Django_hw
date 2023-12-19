from django.shortcuts import render, reverse
import copy

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def recipe_with_serve(request):
    servings = int(request.GET.get('servings', 1))
    path = request.path.replace('/', '')
    new_data = copy.deepcopy(DATA)
    recipe = new_data.get(path)
    if path in new_data:
        for key, val in recipe.items():
            recipe[key] = val * servings
        context = {
            'recipe': recipe,
        }
        print(DATA)
        print(new_data)
        return render(request, 'calculator/index.html', context)
    else:
        recipe = path
        context = {
            'recipe': recipe,
        }
        return render(request, 'calculator/index.html', context)


def recipe_book(request):
    template_home = 'home.html'
    pages = {
        'Омлет обыкновенный': reverse('omlet'),
        'Паста а-ля Руссо': reverse('pasta'),
        'Бутер, очень вкусный': reverse('buter')
    }
    context = {
        'pages': pages
    }
    return render(request, template_home, context)
