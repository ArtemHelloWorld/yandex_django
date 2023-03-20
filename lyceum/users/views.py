import django.conf
import django.contrib.auth.decorators
import django.contrib.auth.forms
import django.contrib.auth.models
import django.shortcuts
import users.forms
import users.models
import users.services


def signup(request):
    signup_form = users.forms.SignUpForm(request.POST or None)

    if signup_form.is_valid():
        user = signup_form.save(commit=False)

        if django.conf.settings.ACTIVATE_USERS:
            user.is_active = True
            user.save()
            return django.shortcuts.redirect("users:login")
        else:
            user.is_active = False
            user.save()

            users.services.send_email_with_registration_link(request, user)

            return django.shortcuts.redirect("users:signup_complete")

    context = {
        "form": signup_form,
    }

    return django.shortcuts.render(request, "users/signup/signup.html", context)


def signup_complete(request):
    return django.shortcuts.render(
        request=request,
        template_name="users/signup/signup_complete.html",
    )


def signup_activate(request, activation_code):
    user = users.services.validate_activation_link(activation_code)
    if user and not user.is_active:
        user.is_active = True
        user.save()
        users.models.Profile.objects.create(user=user)

        message = "Вы успешно зерегистрировались"

    else:
        message = "Неверная ссылка или действие ссылки истекло"

    context = {"message": message}

    return django.shortcuts.render(
        request=request,
        template_name="users/signup/signup_done.html",
        context=context,
    )


def users_list(request):
    users_qs = django.contrib.auth.models.User.objects.filter(
        is_active=True
    ).only("username")

    context = {
        "users": users_qs,
    }

    return django.shortcuts.render(
        request=request, template_name="users/profile/users_list.html", context=context
    )


def user_detail(request, user_id):
    user_info = (
        django.contrib.auth.models.User.objects.select_related("profile")
        .only(
            "email",
            "username",
            "first_name",
            "last_name",
            "profile__birthday",
            "profile__image",
            "profile__coffee_count",
        )
        .get(id=user_id)
    )

    context = {
        "user_info": user_info,
    }
    return django.shortcuts.render(
        request=request,
        template_name="users/profile/user_detail.html",
        context=context,
    )


@django.contrib.auth.decorators.login_required
def profile(request):
    user = request.user
    user_form = users.forms.UserForm(instance=user)
    profile_form = users.forms.UserProfileForm(instance=user.profile)

    if request.method == "POST":
        user_form = users.forms.UserForm(request.POST, instance=user)
        profile_form = users.forms.UserProfileForm(
            request.POST, request.FILES, instance=user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }

    return django.shortcuts.render(request, "users/profile/profile.html", context)
