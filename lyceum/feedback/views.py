import django.contrib.messages
import django.shortcuts

import feedback.forms
import feedback.services


def feedback_render(request):
    if request.method == "POST":
        form = feedback.forms.FeedbackForm(request.POST, request.FILES)

        if form.is_valid():
            text = form.cleaned_data["text"]
            email = form.cleaned_data["email"]

            feedback.services.add_feedback_to_db(
                text, email, request.FILES.getlist("files")
            )

            feedback.services.send_feedback_mail(text, email)

            django.contrib.messages.success(request, "Письмо отправлено!")

            return django.shortcuts.redirect("feedback:feedback")

    else:
        form = feedback.forms.FeedbackForm()

    context = {"form": form}

    return django.shortcuts.render(
        request=request,
        template_name="feedback/feedback.html",
        context=context,
    )


def feedback_check(request):
    form = feedback.forms.FeedbackCheckForm(request.POST or None)

    context = {"form": form}

    if form.is_valid():
        email = form.cleaned_data["email"]
        feedbacks = feedback.services.get_feedbacks_by_email(email)

        if feedbacks.count():
            context["feedbacks"] = feedbacks
        else:
            django.contrib.messages.error(request, "Такой почты нет")
            return django.shortcuts.redirect("feedback:feedback_check")

    return django.shortcuts.render(
        request=request,
        template_name="feedback/feedback_check.html",
        context=context,
    )


def feedback_detail(request, feedback_id_code):
    feedback_item = feedback.services.get_feedback_by_pk(feedback_id_code)

    context = {"feedback_item": feedback_item}

    return django.shortcuts.render(
        request=request,
        template_name="feedback/feedback_detail.html",
        context=context,
    )
