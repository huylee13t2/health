from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from account.models import CWGHMOUser


def get_content_type() -> ContentType:
    try:
        return ContentType.objects.get_for_model(CWGHMOUser)
    except:
        return None


def create_default_permissions():
    ct = get_content_type()
    if not ct:
        return
    Permission.objects.get_or_create(codename='private_customer', name='Private Customer', content_type=ct)
    Permission.objects.get_or_create(codename='corporate_customer', name='Corporate Customer', content_type=ct)
    Permission.objects.get_or_create(codename='provider', name='Provider', content_type=ct)
    Permission.objects.get_or_create(codename='hmo', name='HMO', content_type=ct)
    Permission.objects.get_or_create(codename='platform_admin', name='Platform Admin', content_type=ct)
    Permission.objects.get_or_create(codename='cwg_admin', name='CWG Admin', content_type=ct)
    Permission.objects.get_or_create(codename='org_admin', name='Organization Admin', content_type=ct)

create_default_permissions()
