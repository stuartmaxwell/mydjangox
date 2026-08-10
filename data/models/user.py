"""The User model."""

import logging
import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

logger = logging.getLogger(__name__)


class UserManager(BaseUserManager):
    """Custom user manager for the User model."""

    def _create_user(
        self,
        *,
        email: str,
        password: str | None = None,
        **extra_fields: bool | None,
    ) -> User:
        """Private method to create and return a user with an email, password, and other fields.

        Note: `.lower()` is added to the email normalisation since `normalize_email()` only converts the email domain to
        lowercase. But in the real world, email addresses are almost always case-insensitive.
        """
        email = self.normalize_email(email).lower()
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, password: str | None = None, **extra_fields: bool) -> User:
        """Create and return a regular user with an email and password."""
        extra_fields.setdefault("is_staff", False)  # set this manually in the admin
        extra_fields.setdefault("is_superuser", False)  # use create_superuser to create
        return self._create_user(
            email=email,
            password=password,
            **extra_fields,
        )

    def create_superuser(self, email: str, password: str | None = None, **extra_fields: bool) -> User:
        """Create and return a superuser with an email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_email_verified", True)

        # If the following fields are false, then something odd is going on - raise an error.
        if extra_fields.get("is_staff") is not True:
            msg = "Superuser must have is_staff=True."
            raise ValueError(msg)
        if extra_fields.get("is_superuser") is not True:
            msg = "Superuser must have is_superuser=True."
            raise ValueError(msg)

        return self._create_user(
            email=email,
            password=password,
            **extra_fields,
        )


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that extends the default Django user model.

    Important notes:
    - This model uses email as the unique identifier instead of username.
    - The `UserManager` is used to handle user creation and management.
    - The `USERNAME_FIELD` is set to 'email', which is required for authentication.
    - UUIDField is used for the `id` field to provide a unique identifier for each user.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField("email address", unique=True)
    is_email_verified = models.BooleanField(
        "email verified",
        default=False,
        help_text="Designates whether this user's email address has been verified.",
    )
    # Standard Django fields
    # Note: omitting the following fields: username, first_name, last_name
    # Note: is_superuser is not included as it is managed by the PermissionsMixin
    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text=(
            "Designates whether this user should be treated as active. Unselect this instead of deleting users."
        ),
    )
    date_joined = models.DateTimeField("date joined", default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        """Meta class for the User model."""

        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self) -> str:
        """Return the string representation of the user."""
        return str(self.email)
