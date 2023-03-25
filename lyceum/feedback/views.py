import django.contrib.messages
import django.shortcuts
import django.urls
import django.views.generic

import feedback.forms
import feedback.models
import feedback.services


class FeedbackView(django.views.generic.FormView):
    template_name = "feedback/feedback.html"
    form_class = feedback.forms.FeedbackForm
    success_url = "/feedback/"

    def form_valid(self, form):
        text = form.cleaned_data["text"]
        email = form.cleaned_data["email"]
        files = self.request.FILES.getlist("files")

        feedback.services.add_feedback_to_db(text, email, files)

        feedback.services.send_feedback_mail(text, email)

        django.contrib.messages.success(self.request, "Письмо отправлено!")
        return django.shortcuts.redirect("feedback:feedback")
