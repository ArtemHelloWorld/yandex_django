import django.shortcuts


def description(request):
    context = {
        "title": "Описание",
        "content": "О проекте",
    }
    return django.shortcuts.render(
        request=request,
        template_name="about/description.html",
        context=context,
    )
