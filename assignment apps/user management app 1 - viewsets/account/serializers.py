from rest_framework import serializers
from core.models import User


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "address",
            "is_manager",
        ]
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
