from django.urls import path, reverse_lazy
from Accounts import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.register, name='register'),
    path('Login', views.Login, name='Login'),
    path('Logout',views.Logout, name='Logout'),

    #Password Reset Urls path

    path('reset_password',auth_views.PasswordResetView.as_view(template_name="reset_password.html",
                                                               success_url=reverse_lazy('reset_password_done')),
         name="reset_password"),

    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),
         name="reset_password_sent"),

    path('password_reset_confirm<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html",
                                                            success_url=reverse_lazy('reset_password_done')),
         name="password_reset_confirm"),

    path('reset_password_done',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
         name="reset_password_done"),
]