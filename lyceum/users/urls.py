import django.conf
import django.contrib.auth.views
import django.urls

import catalog.converters
import users.forms
import users.views

app_name = "users"

django.urls.register_converter(
    catalog.converters.CustomPositiveIntegerConverter, "customint"
)


urlpatterns = [
    django.urls.path(
        "login/",
        django.contrib.auth.views.LoginView.as_view(
            template_name="users/login/login.html",
            form_class=users.forms.CustomAuthenticationForm,
        ),
        name="login",
    ),
    django.urls.path(
        "logout/",
        django.contrib.auth.views.LogoutView.as_view(),
        name="logout",
    ),
    django.urls.path(
        "password_change/",
        django.contrib.auth.views.PasswordChangeView.as_view(
            template_name="users/password_change/password_change.html"
        ),
        name="password_change",
    ),
    django.urls.path(
        "password_change/done/",
        django.contrib.auth.views.PasswordChangeDoneView.as_view(
            template_name="users/password_change/password_change_done.html"
        ),
        name="password_change_done",
    ),
    django.urls.path(
        "password_reset/",
        django.contrib.auth.views.PasswordResetView.as_view(
            template_name="users/password_reset/password_reset.html",
            from_email=django.conf.settings.DEFAULT_FROM_EMAIL,
        ),
        name="password_reset",
    ),
    django.urls.path(
        "password_reset/done/",
        django.contrib.auth.views.PasswordResetDoneView.as_view(
            template_name="users/password_reset/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    django.urls.path(
        "reset/<uidb64>/<token>/",
        django.contrib.auth.views.PasswordResetConfirmView.as_view(
            template_name="users/password_reset/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    django.urls.path(
        "reset/done/",
        django.contrib.auth.views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    django.urls.path(
        "signup/", users.views.SignupView.as_view(), name="signup"
    ),
    django.urls.path(
        "signup_complete/",
        users.views.SignupCompleteView.as_view(),
        name="signup_complete",
    ),
    django.urls.path(
        "signup/activate/<str:activation_code>",
        users.views.SignupActivateView.as_view(),
        name="signup_activate",
    ),
    django.urls.path(
        "back/activate/<str:activation_code>",
        users.views.BackActivateView.as_view(),
        name="back_activate",
    ),
    django.urls.path(
        "users_list/", users.views.UsersListView.as_view(), name="users_list"
    ),
    django.urls.path(
        "user_detail/<customint:user_id>/",
        users.views.UserDetail.as_view(),
        name="user_detail",
    ),
    django.urls.path(
        "profile/", users.views.ProfileView.as_view(), name="profile"
    ),
]
