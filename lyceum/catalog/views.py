import django.http


def item_list(request):
    return django.http.HttpResponse("<body>Список, элементов</body>")


def item_detail(request, item_pk):
    return django.http.HttpResponse("<body>Подробно элемент</body>")


def item_detail_re(request, reint):
    return django.http.HttpResponse("<body>re path</body>")


def custom_converter(request, custom_int):
    return django.http.HttpResponse("<body>custom int path</body>")
