from rest_framework import serializers

from core.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','email','password','address','is_manager']

    def create(self, validated_data):
        user = User.objects.create(
            first_name = validated_data.get('first_name'),
            last_name = validated_data.get('last_name'),
            email = validated_data.get('email'),
            address = validated_data.get('address'),
            is_manager = validated_data.get('is_manager'),
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.email = validated_data.get('email',instance.email)
        instance.address = validated_data.get('address',instance.address)
        instance.is_manager = validated_data.get('is_manager',instance.is_manager)
        instance.set_password(validated_data.get('password',instance.password))
        instance.save()
        return instance
    