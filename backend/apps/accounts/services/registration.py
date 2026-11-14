from django.contrib.auth import get_user_model
from django.db import transaction, IntegrityError
from django.core.exceptions import ValidationError
from utils.service_result import ServiceResult
from apps.accounts.services.otp_service import PhoneOTPService, EmailOTPService


User = get_user_model()


class UserRegistration:


    @staticmethod
    def registration(self, first_name, last_name,phone_number, email,
                     password, date_of_birth=None):

        if  not first_name :
            return ServiceResult.fail(
            message="first name is required")
        
        if  not last_name :
            return ServiceResult.fail(
            message="last name is required")
        
        if not password :
             return ServiceResult.fail(
            message="password is required")

        if not phone_number :
            return ServiceResult.fail(
            message="phone number is required")


        if User.objects.filter(phone_number=phone_number).exists():
            return ServiceResult.fail(
            message="this phone number is already registered",
            code="PHONE_TAKEN")

        if User.objects.filter(email=email).exists():
            return ServiceResult.fail(
            message="this email is already registered",
            code="EMAIL_TAKEN")


        try:
            user = User.objects.create_user(
                phone_number=phone_number,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth
            )

            return ServiceResult.success(
                message="User created successfully!",
                data= user
            )

        except IntegrityError:
            return ServiceResult.fail(
                message="A user with this email or phone number already exists."
            )
