from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from core.models import User, ForgetPassword
from .serializers import AccountSerializer, PasswordResetSeralizer, EmterOTPSeralizer, NewPasswordSerailizer, CheckPasswordSeralizer
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
import random, string, datetime
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework.throttling import ScopedRateThrottle
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate


class AccountView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    permission_classes = []
    authentication_classes = []


@extend_schema(tags=['password reset'])
class PasswordResetView(APIView):
    serializer_class = PasswordResetSeralizer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'email_send_throttle'

    def post(self, request):
        data = request.data
        email = data.get('forget_email')
        
        if User.objects.filter(email=email).exists():
            letters = string.ascii_letters + string.digits
            otp = ''.join(random.choice(letters) for _ in range(5))

            while True:
                if ForgetPassword.objects.filter(generated_otp=otp).exists():
                    letters = string.ascii_letters + string.digits
                    otp = ''.join(random.choice(letters) for _ in range(5))
                    continue 
                else:
                    generatedotp = otp
                    break

            try:
                passwd = ForgetPassword.objects.create(
                forget_email = email,
                generated_otp = otp,
                generated_datetime = datetime.datetime.now()
                )
                passwd.save()

                # sedning email
                msg = f"Your Reset Password OTP: {otp}"

                try:
                    send_mail(
                    'Subject here',
                    msg,
                    'anirbanmishra7005@gmail.com',
                    [email],
                    fail_silently=False,
                    )

                    return Response({"status":"password sent to registsred email successfully"})
                
                except Exception as e:
                    print(e)
                    return Response({"status":"email system module error"})    

            except Exception as e:
                print(e)
                return Response({"status":"error"})  

        else:
            return Response({"status":"email not found"})
        
                   
@extend_schema(tags=['password reset'])                   
class EnterOTPView(APIView):
    serializer_class = EmterOTPSeralizer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'enter_otp_throttle'

    def post(self, request):
        data = request.data
        email = data.get('forget_email')
        otp = data.get('otp')

        try:
            forget_password_obj = ForgetPassword.objects.get(forget_email=email, generated_otp=otp)
            user = User.objects.get(email=email)

            # You can customize the payload as needed
            # payload = {
            #     'email': user.email,
            #     'first_name': user.first_name,
            #     'last_name': user.last_name,
            #     'otp': otp,
            # }

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({
                'status': 'success',
                'access_token': access_token,
                # 'user_info': payload
            })

        except Exception as e:
            print(e)
            return Response({"status": "Invalid OTP or email"}, status=400)
        

@extend_schema(tags=['password reset'])  
class NewPasswordView(APIView):
    serializer_class = NewPasswordSerailizer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        data = request.data
        
        passwd = data.get("new_password")
        passwd2 = data.get("reenter_new_password")

        if passwd == passwd2:
            if User.objects.filter(id=user.id).exists():
                try:
                    user_obj = User.objects.get(id=user.id)
                    user_obj.set_password(passwd)
                    user_obj.save()
                    
                    return Response({"status":"password reset sucessfully!"})
                except Exception as e:
                    print(e)
                    return Response({"status":"error"})    
            else:
                return Response({"status":"user id not exist"})
        else:
            return Response({"status":"both password not match"})


class CheckPasswordView(APIView):
    serializer_class = CheckPasswordSeralizer

    def post(self, request):
        data = request.data
        email = data.get("email")
        passwd = data.get("password")
        
        user = authenticate(email=email,password=passwd)
        if user:
            return Response({"status":"match"})
        else:
            return Response({"status":"not match"})



