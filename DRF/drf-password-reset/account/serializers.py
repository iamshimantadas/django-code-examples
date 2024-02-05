from rest_framework import serializers
from core.models import User, ForgetPassword
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']
        extra_kwargs = {"password": {"write_only": True}}


    def create(self, validated_data):
        # Hash the password before saving the user
        password = validated_data.pop("password", None)
        instance = super(AccountSerializer, self).create(validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
        return instance


    def update(self, instance, validated_data):
        # Handle password update separately
        password = validated_data.pop("password", None)
        # Update other fields
        instance = super(AccountSerializer, self).update(instance, validated_data)
        # Update the password if provided
        if password is not None:
            instance.set_password(password)
            instance.save()
        return instance    
    

class PasswordResetSeralizer(serializers.ModelSerializer):
    class Meta:
        model = ForgetPassword
        fields = ['forget_email']

class EmterOTPSeralizer(serializers.Serializer):
    forget_email = serializers.CharField(max_length=50)
    otp = serializers.CharField(max_length=10)

class NewPasswordSerailizer(serializers.Serializer):
    new_password = serializers.CharField(max_length=50)
    reenter_new_password = serializers.CharField(max_length=50)
    token = serializers.CharField(max_length=250)

class CheckPasswordSeralizer(serializers.Serializer):
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=50)   