from django.shortcuts import render

# Create your views here.
def platform(request):
    pagename = {'main': "Главная страница", 'games': "Игры", 'cart': 'Корзина'}
    menu = {'platform': 'Главная', 'shop': "Магазин", 'cart_n': 'Корзина'}
    content = {'games': ['Atomic Heart', "Cyberpunk 2077", 'PayDay 2',],
               'error': "Извините, ваша корзина пуста"}
    return render(request,"platform.html", content, pagename, menu)

