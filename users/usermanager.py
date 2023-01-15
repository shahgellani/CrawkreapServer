from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    # def create_user_without_password(self, email, name, phone):
    #     if not email:
    #         raise ValueError("ENTER AN EMAIL BUDDY")
    #     if not name:
    #         raise ValueError("I KNOW YOU HAVE A NAME")
    #     if not phone:
    #         raise ValueError("ENTER YOUR PHONE NUMBER")
    #
    #     user = self.model(
    #         email=self.normalize_email(email),
    #         name=name,
    #         phone=phone,
    #         )
    #     user.has_usable_password()
    #     user.is_superuser = False
    #     user.save()
    #
    #     return user

    def create_user(self, email, username, password):
        if not email:
            raise ValueError("ENTER AN EMAIL BUDDY")
        if not username:
            raise ValueError("I KNOW YOU HAVE A NAME")
        if not password:
            raise ValueError("PASSWORD?!?!?!? HELLO??")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.is_superuser = False
        user.save()

        return user

    def create_superuser(self, email, username, password, phone=None):
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

    def create_inactive_user(self, username, email, password):
        user = self.create_user(email, username, password)
        user.is_active = False
        user.save()
        return user