import catalog.models
import django.db.models
import django.http
import django.shortcuts


def home(request):
    items = catalog.models.Item.objects.published(is_on_main=True)

    context = {
        "title": "Главная",
        "content": "Главная",
        "items": items,
    }
    return django.shortcuts.render(
        request=request, template_name="homepage/home.html", context=context
    )


def error418(request):
    return django.http.HttpResponse("<body>Я чайник.</body>", status=418)
