import django.urls

import feedback.views

app_name = "feedback"

urlpatterns = [
    django.urls.path(
        "", feedback.views.FeedbackView.as_view(), name="feedback"
    ),
    django.urls.path(
        "check/",
        feedback.views.FeedbackCheckView.as_view(),
        name="feedback_check",
    ),
    django.urls.path(
        "<str:feedback_id_code>/",
        feedback.views.FeedbackDetailView.as_view(),
        name="feedback_detail",
    ),
]
