from django.shortcuts import render

from .models import MenuItem


def index(request):
    menu_items = MenuItem.objects.all()
    # Рендерим шаблон
    return render(request, 'menu.html', {'menu_items': menu_items})
