import django.db.models
import django.http
import django.shortcuts
import django.views.generic
import rating.forms
import rating.models


class DeleteView(django.views.generic.View):
    def post(self, request: django.http.HttpRequest, item_pk: int):
        review = django.shortcuts.get_object_or_404(
            rating.models.Review,
            user=request.user,
            item__id=item_pk,
        )

        review.delete()

        return django.shortcuts.redirect(
            "catalog:item_detail", item_pk=item_pk
        )
