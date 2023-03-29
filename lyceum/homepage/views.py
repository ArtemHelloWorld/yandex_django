import django.db.models
import django.http
import django.shortcuts
import django.views.generic

import catalog.models


class HomeView(django.views.generic.ListView):
    template_name = "homepage/home.html"
    context_object_name = "items"
    paginate_by = 18

    def get_queryset(self):
        return catalog.models.Item.objects.published(
            is_on_main=True, ordering="name"
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная"
        return context


class Error418(django.views.generic.View):
    def get(self, request):
        if self.request.user.is_authenticated:
            self.request.user.profile.coffee_count += 1
            self.request.user.profile.save()

        return django.http.HttpResponse("<body>Я чайник.</body>", status=418)
