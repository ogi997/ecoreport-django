from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class MyModelBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        #print(f"test {UserModel.password}")
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)

        try:
            username_field = '{}__iexact'.format(UserModel.USERNAME_FIELD)
            user = UserModel._default_manager.get(**{username_field: username})
            print(f"aaa {user.password}")
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            print(f"password {password} user.password {user.password} and {user.check_password(password)}")
            if user.check_password(password) and self.user_can_authenticate(user):
                print(f"ccc {user}")
                return user
