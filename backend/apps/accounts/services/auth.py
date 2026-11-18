from django.contrib.auth import get_user_model
from utils.service_result import ServiceResult



User = get_user_model()


class LoginService:

    def __init__(self, phone_number, password):
        self.phone_number = phone_number
        self.password = password



    def login(self):

        try :
            user = User.objects.get(phone_number=self.phone_number)

        except User.DoesNotExist:
            return ServiceResult.fail(
                message="Invalid phone number or password",
                # for security matter 
            )

        if not user.is_active:
            return ServiceResult.fail(
                message="user account has been deactivated",
                code="DEACTIVATED_USER"
            )

        if not user.check_password(self.password):
            return ServiceResult.fail(
                message="Invalid phone number or password"
            )

        return ServiceResult.success(
            message="You are logged in",
            data={'user':user}
        )




class ChangePasswordService:
    """
    Change password for authenticated users.
    User must provide old password for security.
    """
    
    def __init__(self, user):

        self.user = user
    
    def change_password(self, old_password, new_password, confirm_password):

        """
        Change password after validating old password.
        """

        
        if not self.user.check_password(old_password):
            return False, "Current password is incorrect."
        
        if new_password != confirm_password:
            return False, "New passwords do not match."
        
        if old_password == new_password:
            return False, "New password must be different from current password."
        
        self.user.set_password(new_password)
        self.user.save(update_fields=['password'])
        
        return True, "Password changed successfully."