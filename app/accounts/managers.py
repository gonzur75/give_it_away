from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custoom user model manager where name is the unique identifiers
    for authentication
    """
    def create_user(self, name, password, **extra_fields):
        """Create and save a User with given name and password"""
        if not name:
            raise ValueError(_('The email must be set'))
        name = self.name
        user = self.model(name=name, **extra_fields)
        user.set_password(password)
        user.save()
        return user
