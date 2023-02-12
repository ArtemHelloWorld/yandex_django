from django.http import HttpResponse


def item_list(request):
    return HttpResponse("<body>Список элементов</body>")


def item_detail(request, item_pk):
    return HttpResponse("<body>Подробно элемент</body>")


def item_detail_re(request, reint):
    return HttpResponse("<body>re path</body>")


def custom_converter(request, custom_int):
    return HttpResponse("<body>custom int path</body>")
