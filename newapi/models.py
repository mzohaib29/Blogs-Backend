# # # models.py
# # from django.db import models
# # from django.contrib.auth.models import AbstractUser

# # class User(AbstractUser):
# #     email = models.EmailField(unique=True)

# #     USERNAME_FIELD = 'email'
# #     REQUIRED_FIELDS = ['username']






# from django.db import models
# from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager)
# from uuid import uuid4

# class UserManager(BaseUserManager):

#     def create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError()
#         user = self.model(email=self.normalize_email(email), **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
    
#     def create_superuser(self, email, password):
#         user = user.create_user(email=email, password=password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
#         return user


# class User(AbstractBaseUser, PermissionsMixin):
#     id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     email = models.EmailField(unique=True)
#     is_staff = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     objects = UserManager()