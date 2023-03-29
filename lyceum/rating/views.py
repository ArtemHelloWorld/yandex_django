import django.db.models
import django.http
import django.shortcuts
import django.views.generic

import rating.forms
import rating.models


class DeleteView(django.views.generic.View):
    form_class = rating.forms.DeleteReviewForm
    
    def post(self, request: django.http.HttpRequest, item_pk: int):
        form = self.form_class(request.POST)

        if form.is_valid():
            review: rating.models.Review = rating.models.Review.objects.get_rating(
                user=request.user, 
                item__id=item_pk,
            )
            
            review.delete()

        django.shortcuts.redirect("catalog:item_detail", item_pk=item_pk)