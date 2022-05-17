from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirmation = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'password', 'password_confirmation', 'email', 'image')

    def validate(self, params):
        if params['password'] != params['password_confirmation']:
            raise serializers.ValidationError({"password": "Password fields didn't macth."})
        return params

    def create(self, validated_data):
        user = User.objects.create(
            name=validated_data['name'],
            email=validated_data['email'],
            image=validated_data['image']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class JwtTokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(JwtTokenSerializer, cls).get_token(user)

        token['email'] = user.email
        return token


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'image')
        extra_kwargs = {
            'name': {'required': True}
        }

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.image = validated_data['image']

        instance.save()

        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'image')
