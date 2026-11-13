from apps.accounts.models.otp import PhoneOTP, EmailOTP
import random
from django.utils import timezone
from datetime import timedelta
from django.db import transaction
from utils.service_result import ServiceResult  
from django.contrib.auth.hashers import make_password, check_password

class OTPService:

    OTP_MIN = 111111
    OTP_MAX = 999999
    COOLDOWN_SECONDS = 60


    otp_model = None
    identifier_field = None
    EXPIRY_TIME = None
    MAX_ATTEMPT = None
    

    def __init__(self, identifier):
        self.identifier = identifier



    def generate_code(self):
        return random.randint(self.OTP_MIN, self.OTP_MAX)



    def send_otp(self, code):

        raise NotImplementedError(
            "child classes must implement send_otp()"
        )


    def get_identifier(self):

        return {self.identifier_field:self.identifier}

    
    def can_request(self):

        now = timezone.now()

        recent_request = self.otp_model.objects.filter(
            **self.get_identifier(),
            created_at__gte = now - timedelta(
                seconds=self.COOLDOWN_SECONDS
            )
        ).first()

        if recent_request:
            wait_time = self.COOLDOWN_SECONDS - int(
                (now - recent_request.created_at).total_seconds()
            )

            return ServiceResult.fail(
                message=f"please wait {max(wait_time, 0)} secondes before asking a new OTP",
                code = "COOLDOWN_ACTIVE"
            )

        return ServiceResult.success(
            message="can request OTP"
        )


    def create_otp(self):

        can_request_result = self.can_request()

        if not can_request_result.success:

            return can_request_result


        code = self.generate_code()
        code_hash = make_password(code)
        now = timezone.now()

        self.otp_model.objects.update_or_create(

            **self.get_identifier(),
            defaults={
                "code":code_hash,
                "attempts": 0,
                "created_at": now,
                "expired_at": now + timedelta(minutes=self.EXPIRY_TIME),
            })

        send_otp_status = self.send_otp()
        if send_otp_status:
            return ServiceResult.success(
                message="OTP sended successfully!",
                data=self.get_identifier()
            )

        else:
            self.otp_model.objects.filter(**self.get_identifier()).delete()
            return ServiceResult.fail(
                message="Failed to send the OTP, try again later",
                code="SEND_OTP_FAILED"
            )

        

        