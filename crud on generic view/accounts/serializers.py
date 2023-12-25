from rest_framework import serializers

from core.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','email','password', 'address','is_manager','is_staff','is_superuser']

    def create(self, validated_data):
        user = User.objects.create(
            first_name = validated_data.get('first_name'),
            last_name = validated_data.get('last_name'),
            email = validated_data.get('email'),
            address = validated_data.get('address'),
            is_manager = validated_data.get('is_manager'),
            is_staff = validated_data.get('is_staff')
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user