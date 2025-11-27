from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    
    def create_user(self,email,password = None,**extra_fields):
        if email is None:
            raise ValueError("Email Is Required")
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    # create super user
    def create_superuser(self,email,password = None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuse Must be Staff")  
        if not extra_fields.get('is_staff'):
            raise ValueError("Superuse Must be Staff")
        return self.create_user(email,password,**extra_fields)