import catalog.models
import django.db.models
import django.http
import django.shortcuts


def item_list(request):
    items = catalog.models.Item.objects.published()
    context = {
        "title": "Каталог",
        "items": items,
    }
    return django.shortcuts.render(
        request=request,
        template_name="catalog/item_list.html",
        context=context,
    )


def item_detail(request, item_pk):
    item = django.shortcuts.get_object_or_404(
        catalog.models.Item.objects.published().prefetch_related(
            "gallery",
        ),
        pk=item_pk,
    )

    context = {
        "content": f"Подробно элемент. Pk:{item_pk}",
        "item": item,
    }
    return django.shortcuts.render(
        request=request,
        template_name="catalog/item_detail.html",
        context=context,
    )
