import django.forms
import rating.models


class BootstrapWidgetsForm(django.forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"


class ReviewForm(BootstrapWidgetsForm):
    class Meta:
        model = rating.models.Review
        fields = (rating.models.Review.rating.field.name,)


class DeleteReviewForm(BootstrapWidgetsForm):
    class Meta:
        model = rating.models.Review
        fields = ()
