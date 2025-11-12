from extras.plugins import PluginConfig

class ExternalLinksSuperuserConfig(PluginConfig):
    name = 'external_links_superuser'
    verbose_name = 'External Links for Superuser'
    description = 'Adds a custom left sidebar menu with external links visible only to superusers'
    version = '1.0.0'
    author = 'Your Name'
    author_email = 'you@example.com'

config = ExternalLinksSuperuserConfig
