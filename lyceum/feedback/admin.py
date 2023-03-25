import django.contrib.admin

import feedback.models


class FeedbackFileInline(django.contrib.admin.StackedInline):
    model = feedback.models.FeedbackFile
    extra = 1


@django.contrib.admin.register(feedback.models.Feedback)
class FeedbackAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        feedback.models.Feedback.created_on.field.name,
        feedback.models.Feedback.status.field.name,
    )
    list_editable = (feedback.models.Feedback.status.field.name,)
    list_display_links = (feedback.models.Feedback.created_on.field.name,)
    inlines = [
        FeedbackFileInline,
    ]
