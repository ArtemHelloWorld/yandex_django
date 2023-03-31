import django.contrib.messages
import django.db.models
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


class FeedbackCheckView(django.views.generic.View):
    form_class = feedback.forms.FeedbackCheckForm
    template_name = "feedback/feedback_check.html"

    def get(self, request):
        form = self.form_class()
        return django.shortcuts.render(
            request, self.template_name, {"form": form}
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]

            feedbacks = feedback.services.get_feedbacks_by_email(email)

            if len(feedbacks):
                return django.shortcuts.render(
                    request,
                    self.template_name,
                    {"form": form, "feedbacks": feedbacks},
                )
            else:
                django.contrib.messages.error(request, "Такой почты нет")
                return django.shortcuts.redirect("feedback:feedback_check")
        else:
            return django.shortcuts.render(
                request, self.template_name, {"form": form}
            )


class FeedbackDetailView(django.views.generic.DetailView):
    template_name = "feedback/feedback_detail.html"
    pk_url_kwarg = "feedback_id_code"
    context_object_name = "feedback_item"

    def get_object(self, queryset=None):
        feedback_id_code = self.kwargs.get(self.pk_url_kwarg)
        return feedback.services.get_feedback_by_id_code(feedback_id_code)
