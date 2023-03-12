import django.contrib.messages
import django.shortcuts
import feedback.forms
import feedback.services


def feedback_render(request):
    form = feedback.forms.FeedbackForm(request.POST or None)
    context = {"title": "Обратная связь", "form": form}
    if request.method == "POST":
        if form.is_valid():
            text = form.cleaned_data["text"]
            email = form.cleaned_data["email"]

            feedback.services.send_feedback_mail(text, email)

            django.contrib.messages.success(request, "Письмо отправлено!")

            return django.shortcuts.redirect("feedback:feedback")

    return django.shortcuts.render(
        request=request,
        template_name="feedback/feedback.html",
        context=context,
    )
