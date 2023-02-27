import catalog.models
import django.http
import django.shortcuts


def item_list(request):
    context = {
        "title": "Каталог",
        "items": catalog.models.Item.objects.filter(is_published=True),
    }
    return django.shortcuts.render(
        request=request,
        template_name="catalog/item_list.html",
        context=context,
    )


def item_detail(request, item_pk):
    context = {
        "title": f"Товар {item_pk}",
        "content": f"Подробно элемент. Pk:{item_pk}",
    }
    return django.shortcuts.render(
        request=request,
        template_name="catalog/item_detail.html",
        context=context,
    )
