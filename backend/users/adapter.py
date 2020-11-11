from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        path = "/api/v1/rest-auth/login/"
        return path