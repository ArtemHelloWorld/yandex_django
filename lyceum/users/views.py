import django.conf
import django.contrib.auth.decorators
import django.contrib.auth.forms
import django.contrib.auth.mixins
import django.contrib.auth.models
import django.shortcuts
import django.views.generic

import users.forms
import users.models
import users.services


class SignupView(django.views.generic.FormView):
    template_name = "users/signup/signup.html"
    form_class = users.forms.SignUpForm

    def form_valid(self, form):
        user = form.save(commit=False)

        if django.conf.settings.ACTIVATE_USERS:
            user.is_active = True
            user.save()
            users.models.Profile.objects.create(user=user)

            return django.shortcuts.redirect("users:login")
        else:
            user.is_active = False
            user.save()

            users.services.send_email_with_activation_link(self.request, user)

            return django.shortcuts.redirect("users:signup_complete")


class SignupCompleteView(django.views.generic.TemplateView):
    template_name = "users/signup/signup_complete.html"


class SignupActivateView(django.views.generic.TemplateView):
    template_name = "users/signup/activation_done.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = users.services.validate_activation_link(
            kwargs.get("activation_code"), hours=12
        )

        if user and not user.is_active:
            user.is_active = True
            user.save()
            users.models.Profile.objects.create(user=user)

            context["message"] = "Вы успешно зерегистрировались"

        else:
            context["message"] = "Неверная ссылка или действие ссылки истекло"


class BackActivateView(django.views.generic.TemplateView):
    template_name = "users/signup/activation_done.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = users.services.validate_activation_link(
            kwargs.get("activation_code"), days=7
        )

        if user and not user.is_active:
            user.is_active = True
            user.save()

            context["message"] = "Вы успешно восставновили аккаунт"

        else:
            context["message"] = "Неверная ссылка или действие ссылки истекло"


class UsersListView(django.views.generic.ListView):
    template_name = "users/profile/users_list.html"
    context_object_name = "users"

    def get_queryset(self):
        return django.contrib.auth.models.User.objects.filter(
            is_active=True
        ).only("username")


class UserDetail(django.views.generic.DetailView):
    template_name = "users/profile/user_detail.html"
    pk_url_kwarg = "user_id"
    context_object_name = "user_info"

    def get_queryset(self):
        return users.models.MyUser.objects.only(
            "email",
            "username",
            "first_name",
            "last_name",
            "profile__birthday",
            "profile__image",
            "profile__coffee_count",
        )


class ProfileView(
    django.contrib.auth.mixins.LoginRequiredMixin,
    django.views.generic.TemplateView,
):
    template_name = "users/profile/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        user_form = users.forms.UserForm(instance=user)
        profile_form = users.forms.UserProfileForm(instance=user.profile)

        context["user_form"] = user_form
        context["profile_form"] = profile_form
        return context

    def post(self, request):
        user = request.user
        user_form = users.forms.UserForm(request.POST, instance=user)
        profile_form = users.forms.UserProfileForm(
            request.POST, request.FILES, instance=user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        return django.shortcuts.redirect("users:profile")
