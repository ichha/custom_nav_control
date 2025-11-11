from netbox.plugins import PluginConfig
from django.contrib.auth.signals import user_logged_in
from netbox.registry import registry


def hide_ipam_menu(user):
    """
    Hide the IPAM menu for non-superusers.
    """
    if not user.is_superuser:
        if 'IPAM' in registry['menus']:
            registry['menus'].pop('IPAM', None)


def handle_user_login(sender, user, request, **kwargs):
    """
    Run when a user logs in to remove menus dynamically.
    """
    hide_ipam_menu(user)


# Connect signal
user_logged_in.connect(handle_user_login)


class CustomNavControlConfig(PluginConfig):
    name = 'custom_nav_control'
    verbose_name = 'Custom Navigation Control'
    description = 'Hide IPAM menu for non-superusers'
    version = '1.0'
    author = 'Your Name'
    base_url = 'custom-nav-control'
