import django.db.models
import django.http
import django.shortcuts
import django.views.generic

import catalog.models

NUMBER_OF_ITEMS = 5


class ItemListView(django.views.generic.ListView):
    template_name = "catalog/item_list.html"
    context_object_name = "items"

    def get_queryset(self):
        return catalog.models.Item.objects.published(ordering="category__name")


class ItemDetailView(django.views.generic.DetailView):
    template_name = "catalog/item_detail.html"
    pk_url_kwarg = "item_pk"
    context_object_name = "item"

    def get_queryset(self):
        return catalog.models.Item.objects.published().prefetch_related(
            "gallery",
        )


class DownloadImageMainView(django.views.generic.View):
    def get(self, request, image_pk):
        image = django.shortcuts.get_object_or_404(
            catalog.models.ItemImageMain.objects.select_related("item"),
            pk=image_pk,
        )
        if image.item.is_published:
            image_path = image.image_main.path
            filename = image.image_main.name.split("/")[-1]
            image_file = open(image_path, "rb")

            response = django.http.FileResponse(image_file)
            response["Content-Type"] = "image/jpg"
            response[
                "Content-Disposition"
            ] = f"attachment; filename={filename}"

            return response
        else:
            raise django.http.Http404("This item is not published")


class DownloadImageGalleryView(django.views.generic.View):
    def get(self, request, image_pk):
        image = django.shortcuts.get_object_or_404(
            catalog.models.ItemImageGallery, pk=image_pk
        )
        if image.item.is_published:
            image_path = image.image_gallery.path
            filename = image.image_gallery.name.split("/")[-1]
            image_file = open(image_path, "rb")

            response = django.http.FileResponse(image_file)
            response["Content-Type"] = "image/jpg"
            response[
                "Content-Disposition"
            ] = f"attachment; filename={filename}"

            return response
        else:
            raise django.http.Http404("This item is not published")


class ItemsNewView(django.views.generic.ListView):
    template_name = "catalog/item_unique.html"
    context_object_name = "items"

    def get_queryset(self):
        return catalog.models.Item.objects.this_week(NUMBER_OF_ITEMS)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Новинки"
        context["header"] = "НОВИНКИ ЭТОЙ НЕДЕЛИ!"
        return context


class ItemsFridayView(django.views.generic.ListView):
    template_name = "catalog/item_unique.html"
    context_object_name = "items"

    def get_queryset(self):
        return catalog.models.Item.objects.friday(NUMBER_OF_ITEMS)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Пятница!"
        context["header"] = "ПЯТНИЧНЫЕ НОВИНКИ!"
        return context


class ItemsUnverifiedView(django.views.generic.ListView):
    template_name = "catalog/item_unique.html"
    context_object_name = "items"

    def get_queryset(self):
        return catalog.models.Item.objects.unverified()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Непроверенное"
        context["header"] = "Эти товары ещё не изменялись"
        return context
