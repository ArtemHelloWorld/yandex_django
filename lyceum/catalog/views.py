import random

import catalog.models
import django.db.models
import django.http
import django.shortcuts


def item_list(request):
    items = catalog.models.Item.objects.published(ordering="category__name")
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


def download_image_main(request, image_pk):
    item = django.shortcuts.get_object_or_404(
        catalog.models.Item, image__pk=image_pk
    )
    if item.is_published:
        image = django.shortcuts.get_object_or_404(
            catalog.models.ItemImageMain, pk=image_pk
        )
        image_path = image.image_main.path
        filename = image.image_main.name.split("/")[-1]
        image_file = open(image_path, "rb")

        response = django.http.FileResponse(image_file)
        response["Content-Type"] = "image/jpg"
        response["Content-Disposition"] = f"attachment; filename={filename}"
        return response
    else:
        raise django.http.Http404("This item is not published")


def download_image_gallery(request, image_pk):
    item = django.shortcuts.get_object_or_404(
        catalog.models.ItemImageGallery, pk=image_pk
    ).item
    if item.is_published:
        image = django.shortcuts.get_object_or_404(
            catalog.models.ItemImageGallery, pk=image_pk
        )
        image_path = image.image_gallery.path
        filename = image.image_gallery.name.split("/")[-1]
        image_file = open(image_path, "rb")

        response = django.http.FileResponse(image_file)
        response["Content-Type"] = "image/jpg"
        response["Content-Disposition"] = f"attachment; filename={filename}"
        return response
    else:
        raise django.http.Http404("This item is not published")


def items_new(request):
    number_of_items = 5

    items_ids = catalog.models.Item.objects.this_week()

    if len(items_ids) > number_of_items:
        random_numbers = random.sample(list(items_ids), number_of_items)
    else:
        random_numbers = items_ids

    items = catalog.models.Item.objects.filter(id__in=random_numbers)

    context = {
        "title": "Новинки",
        "header": "НОВИНКИ ЭТОЙ НЕДЕЛИ!",
        "items": items,
    }
    return django.shortcuts.render(
        request=request,
        template_name="catalog/item_unique.html",
        context=context,
    )


def items_friday(request):
    items_ids = catalog.models.Item.objects.friday()[:5]

    items = catalog.models.Item.objects.filter(id__in=list(items_ids))
    context = {
        "title": "Пятница!",
        "header": "ПЯТНИЧНЫЕ НОВИНКИ!",
        "items": items,
    }
    return django.shortcuts.render(
        request=request,
        template_name="catalog/item_unique.html",
        context=context,
    )


def items_unverified(request):
    items = catalog.models.Item.objects.unverified()
    context = {
        "title": "Непроверенное",
        "header": "Эти товары ещё не изменялись",
        "items": items,
    }
    return django.shortcuts.render(
        request=request,
        template_name="catalog/item_unique.html",
        context=context,
    )
