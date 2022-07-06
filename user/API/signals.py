from allauth.account.signals import user_signed_up, user_logged_in
from django.dispatch import receiver

# apps.py / __init__.py 설정
@receiver(user_signed_up)
def complete_social_signed_up(sender, **kwargs):
    print("user: ", kwargs['user'])
    print("request: ", kwargs['request'] )
    
@receiver(user_logged_in)
def complete_social_logged_in(sender, **kwargs):
    print("user: ", kwargs['user'])
    print("request: ", kwargs['request'] )
    