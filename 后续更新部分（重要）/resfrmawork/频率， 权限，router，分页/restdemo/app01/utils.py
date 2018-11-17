

from rest_framework import exceptions

from rest_framework.authentication import BaseAuthentication


from .models import *
class TokenAuth(BaseAuthentication):
    def authenticate(self,request):

        token = request.GET.get("token")
        token_obj = Token.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed("验证失败!")
        else:
            return token_obj.user.name,token_obj.token



class SVIPPermission(object):
    message="只有超级用户才能访问"
    def has_permission(self,request,view):
        username=request.user
        user_type=User.objects.filter(name=username).first().user_type

        if user_type==3:

            return True # 通过权限认证
        else:
            return False