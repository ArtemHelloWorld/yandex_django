import django.urls
import feedback.views


app_name = 'feedback'

urlpatterns = [
    django.urls.path("", feedback.views.feedback_render, name="feedback"),
]
