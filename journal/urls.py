
from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name=''),
    path('my-login', views.my_login, name='my-login'),
    path('user-logout', views.user_logout, name='user-logout'),
    path('register', views.register, name='register'),
    
    # authenticated
    path('dashboard', views.dashboard, name='dashboard'),
    path('create-thought', views.create_thought, name='create-thought'),
    path('my-thoughts', views.my_thoughts, name='my-thoughts'),
    path('update-thought/<str:pk>', views.update_thought, name='update-thought'),
    path('delete-thought/<str:pk>', views.delete_thought, name='delete-thought'),
    
    # Profile Management
    path('profile-management', views.profile_management, name='profile-management'),
    path('delete-account', views.delete_account, name='delete-account'),
    
    # ------   Password Reset: - no custom views, just django builtin views  ---------
    # 1 - Enter email in order to receive password reset link
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="journal/password/password-reset.html"), name='reset_password'),
    
    # 2 - Success Message stating email was sent to reset password
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="journal/password/password-reset-sent.html"), name='password_reset_done'),
    
    #3 - Send link to email, so that user can reset password
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="journal/password/password-reset-form.html"), name='password_reset_confirm'),
    
    # 4 - Show success message that password was changed
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="journal/password/password-reset-complete.html"), name='password_reset_complete'),
        
]
