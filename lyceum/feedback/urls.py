import django.urls
import feedback.views

app_name = "feedback"

urlpatterns = [
    django.urls.path("", feedback.views.feedback_render, name="feedback"),
    django.urls.path(
        "check/", feedback.views.feedback_check, name="feedback_check"
    ),
    django.urls.path(
        "<str:feedback_id_code>/",
        feedback.views.feedback_detail,
        name="feedback_detail",
    ),
]
