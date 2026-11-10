from django.contrib.auth.models import BaseUserManager



class UserManager(BaseUserManager):


    def _create_user(self, phone_number, first_name, last_name,
                     email, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("Phone number is required")
        if not email:
                    raise ValueError("Email is required")
        if not first_name:
            raise ValueError("First name is required")
        if not last_name:
            raise ValueError("Last name is required")

        email = self.normalize_email(email) if email else None

        user = self.model(
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user



    def create_user(self, phone_number, first_name, last_name,
                    email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_admin", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        return self._create_user(
            phone_number, first_name, last_name, email, password, **extra_fields
        )



    def create_superuser(self, phone_number, first_name, last_name,
                         email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_admin") is not True:
            raise ValueError("Superuser must have is_admin=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(
            phone_number, first_name, last_name, email, password, **extra_fields
        )