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

    context = {"title": "Обратная связь", "form": form}

    return django.shortcuts.render(
        request=request,
        template_name="feedback/feedback.html",
        context=context,
    )
