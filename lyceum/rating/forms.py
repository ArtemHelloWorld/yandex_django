import django.forms

import rating.models


class BootstrapWidgetsForm(django.forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            if not isinstance(
                field.field.widget, django.forms.widgets.RadioSelect
            ):
                field.field.widget.attrs["class"] = "form-control"


class ReviewForm(BootstrapWidgetsForm):
    class Meta:
        rating_name = rating.models.Review.rating.field.name
        model = rating.models.Review
        fields = (rating_name,)
        widgets = {rating_name: django.forms.widgets.RadioSelect}
