from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import AccountView, PasswordResetView, EnterOTPView, NewPasswordView, CheckPasswordView

router = SimpleRouter()
router.register("",AccountView)

urlpatterns = [
    path("reset-password/email/",PasswordResetView.as_view()),
    path("reset-password/enter-otp/",EnterOTPView.as_view()),
    path("reset-password/new-password/",NewPasswordView.as_view()),

    # passowrd test url
    path("try-password/",CheckPasswordView.as_view()),

] + router.urls