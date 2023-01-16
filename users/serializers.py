from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User, UserProfile


class UserSerialzer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2',)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs


class RegisterSerializer(serializers.ModelSerializer):
    user = UserSerialzer()

    class Meta:
        model = UserProfile
        fields = ('title', 'dob', 'address', 'country', 'city', 'zip', 'first_name', 'last_name', 'user')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    @classmethod
    def create(cls, validated_data):
        try:
            user_data = validated_data.data.get('user')
            profile_data = validated_data.data
            profile_data.pop("user")
            user = User(**user_data)
            user.set_password(user_data.get("password"))
            user.save()
            user_profile = UserProfile.objects.create(user=user, **profile_data)
            return user_profile
        except:
            pass
        finally:
            pass
        # def update(self, instance, validated_data):
    #         profile_data = validated_data.pop('profile')
    #         profile = instance.profile
    #
    #         instance.email = validated_data.get('email', instance.email)
    #         instance.save()
    #
    #         profile.title = profile_data.get('title', profile.title)
    #         profile.dob = profile_data.get('dob', profile.dob)
    #         profile.first_name = profile_data.get('first_name' , profile.first_name)
    #         profile.last_name = profile_data.get('last_name', profile.last_name )
    #         profile.address = profile_data.get('address', profile.address)
    #         profile.country = profile_data.get('country', profile.country)
    #         profile.city = profile_data.get('city', profile.city)
    #         profile.zip = profile_data.get('zip', profile.zip)
    #         # profile.photo = profile_data.get('photo', profile.photo)
    #         profile.save()
