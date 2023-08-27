from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,  email, password=None):
        # if username is None:
        #     raise TypeError('User must have a username.')
        if email is None:
            raise TypeError('User must have an email address.')
        
        user = self.model(
            # username = username,
            email = self.normalize_email(email),
        )
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self,  email, password=None):
        
        user = self.create_user(
                    email=email,
                    password=password,
                    )
        
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user