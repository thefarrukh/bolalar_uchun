# apps/users/api_endpoints/serializers.py

from rest_framework import serializers

from apps.users.models import Interest, User, UserCourse, UserWebinar


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    interests = InterestSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user


class UserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = "__all__"


class UserWebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWebinar
        fields = "__all__"
