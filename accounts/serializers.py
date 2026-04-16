from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import update_last_login
from rest_framework import serializers, permissions, exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings as jwt_api_settings

from .models import User


class OrganizationTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Login with email + password; pass organization_slug when the email exists in multiple orgs."""

    organization_slug = serializers.SlugField(write_only=True, required=False, allow_null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["organization_slug"] = serializers.SlugField(
            write_only=True, required=False, allow_null=True
        )

    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            "password": attrs["password"],
        }
        org_slug = attrs.get("organization_slug")
        if org_slug is not None:
            authenticate_kwargs["organization_slug"] = org_slug
        try:
            authenticate_kwargs["request"] = self.context["request"]
        except KeyError:
            pass

        self.user = authenticate(**authenticate_kwargs)
        if not jwt_api_settings.USER_AUTHENTICATION_RULE(self.user):
            raise exceptions.AuthenticationFailed(
                self.error_messages["no_active_account"],
                "no_active_account",
            )

        data = {}
        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        if jwt_api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        return data


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'organization', 'role')
    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            organization=validated_data['organization'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
