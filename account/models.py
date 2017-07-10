from django.contrib.auth.models import User
from django.db import models

ACCOUNT_TYPE = (
    ('Private Customer','Private Customer'),
    ('Corporate Customer', 'Corporate Customer'),
    ('Provider', 'Provider'),
    ('HMO', 'HMO'),
)


class CWGHMOUser(models.Model):
    """
    The base user model
    """
    user = models.OneToOneField(User)
    middle_name = models.CharField(max_length=50, default='')
    user_code = models.CharField(max_length=50)
    account_type = models.CharField(max_length=30, choices=ACCOUNT_TYPE)
