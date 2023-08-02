from django.urls import path

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [

    path('profil', views.user_profile, name = 'profil'),

    path('rejestracja', views.register, name = 'rejestracja'),

    path('logowanie', views.login, name = 'logowanie'),

    path('wylogowanie', views.logout, name = 'wylogowanie'),

    path('panel-uzytkownika', views.dashboard, name = 'panel-uzytkownika'),

    path('zarzadzanie-kontem', views.profile_management, name = 'zarzadzanie-kontem'),

    path('usun-konto', views.delete_account, name = 'usun-konto'),

    #Weryfikacja emaila

    path('weryfikacja-emaila/<str:uidb64>/<str:token>/', views.email_verification, name = 'weryfikacja-emaila'),

    path('weryfikacja-emaila-wyslana', views.email_verification_sent, name = 'weryfikacja-emaila-wyslana'),

    path('weryfikacja-emaila-udana', views.email_verification_success, name = 'weryfikacja-emaila-udana'),

    path('weryfikacja-emaila-nieudana', views.email_verification_fail, name = 'weryfikacja-emaila-nieudana'),

    #Zarządzanie hasłem

     # 1 ) Submit our email form

    path('reset_password', auth_views.PasswordResetView.as_view(template_name="account/password-reset.html"), name='reset_password'),


    # 2) Success message stating that a password reset email was sent

    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="account/password-reset-sent.html"), name='password_reset_done'),


    # 3) Password reset link

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="account/password-reset-form.html"), name='password_reset_confirm'),


    # 4) Success message stating that our password was reset

    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="account/password-reset-complete.html"), name='password_reset_complete'),


]