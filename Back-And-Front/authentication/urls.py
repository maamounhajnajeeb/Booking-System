from django.urls import path, include
from . import views

app_name = "authentication"

urlpatterns = [
    
    path("signup/", views.RegisterView.as_view(), name="signup"),
    
    # verify link
    path("email-verify/", views.VerifyEmail.as_view(), name="email_verify"),
    
    # path("mail/", views.html, name="email_sending"),
]
