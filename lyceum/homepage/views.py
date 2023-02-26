import django.http
import django.shortcuts


def home(request):
    context = {
        "title": "Главная",
        "content": "Главная",
    }
    return django.shortcuts.render(
        request=request, template_name="homepage/home.html", context=context
    )


def error418(request):
    return django.http.HttpResponse("<body>Я чайник.</body>", status=418)
