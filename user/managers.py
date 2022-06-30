from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, **extra_fields):
        if username is None:
            raise TypeError('User must have a username.')
        elif email is None:
            raise TypeError('User must have an email address.')
        
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            **extra_fields
        )
        
        user.save()
        
        return user
    
    def create_superuser(self, username, email, **extra_fields):
        
        user = self.create_user(username, email, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        
        return user