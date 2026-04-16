from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model


User = get_user_model()


class OrganizationEmailBackend(BaseBackend):
    """
    Authenticate by email + password, scoped to organization when the same email
    exists in multiple organizations.
    """

    def authenticate(self, request, **kwargs):
        email = kwargs.get(User.USERNAME_FIELD)
        password = kwargs.get("password")
        if email is None or password is None:
            return None

        organization_slug = kwargs.get("organization_slug")
        organization_id = kwargs.get("organization_id")

        qs = User.objects.filter(**{User.USERNAME_FIELD: email})
        if organization_slug is not None:
            qs = qs.filter(organization__slug=organization_slug)
        elif organization_id is not None:
            qs = qs.filter(organization_id=organization_id)

        count = qs.count()
        if count == 0:
            return None
        if count > 1:
            return None

        user = qs.first()
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    @staticmethod
    def user_can_authenticate(user):
        return getattr(user, "is_active", True)
