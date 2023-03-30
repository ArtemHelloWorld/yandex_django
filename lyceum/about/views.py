import django.views.generic


class DescriptionView(django.views.generic.TemplateView):
    template_name = "about/description.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Описание"
        context["content"] = "О проекте"
        return context
