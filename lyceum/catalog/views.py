import django.db.models
import django.http
import django.shortcuts
import django.views.generic
import rating.forms
import rating.models

import catalog.models

NUMBER_OF_ITEMS = 5


class ItemListView(django.views.generic.ListView):
    template_name = "catalog/item_list.html"
    context_object_name = "items"
    paginate_by = 18

    def get_queryset(self):
        return catalog.models.Item.objects.published(ordering="category__name")


class ItemDetailView(django.views.generic.View):
    template_name = "catalog/item_detail.html"
    form_class = rating.forms.ReviewForm
    delete_form_class = rating.forms.DeleteReviewForm

    def get(self, request: django.http.HttpRequest, item_pk: int):
        queryset = catalog.models.Item.objects.published().prefetch_related(
            "gallery",
        )
        item = django.shortcuts.get_object_or_404(queryset, id=item_pk)
        review = (
            rating.models.Review.objects.get_rating(
                user=request.user,
                item=item,
            )
            if request.user.is_authenticated
            else None
        )

        context = {
            "item": item,
            "review_form": self.form_class(instance=review),
            "delete_review_form": self.delete_form_class(),
            "review": review,
        }

        return django.shortcuts.render(request, self.template_name, context)

    def post(self, request, item_pk):
        form = self.form_class(request.POST)

        if form.is_valid():
            rating = form.cleaned_data["rating"]

            review = rating.models.Review.objects.get_rating(
                user=request.user,
                item__id=item_pk,
            ) or rating.models.Review.objects.create(
                user=request.user, item_id=item_pk
            )

            review.rating = rating
            review.save()

        django.shortcuts.redirect("catalog:item_detail", item_pk=item_pk)


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
    paginate_by = 18

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
    paginate_by = 18

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
    paginate_by = 18

    def get_queryset(self):
        return catalog.models.Item.objects.unverified()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Непроверенное"
        context["header"] = "Эти товары ещё не изменялись"
        return context
