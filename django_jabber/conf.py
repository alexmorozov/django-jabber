#--coding: utf8--

from django.conf import settings as _settings


DEFAULTS = {
    'JABBER_DRY_RUN': False,
    'JABBER_USE_TLS': False,
    'JABBER_USE_SSL': False,
}


class DjangoJabberSettings(object):
    """
    Lazy Django settings wrapper for django-jabber
    """
    def __init__(self, wrapped_settings):
        self.wrapped_settings = wrapped_settings

    def __getattr__(self, name):
        if hasattr(self.wrapped_settings, name):
            return getattr(self.wrapped_settings, name)
        elif name in DEFAULTS:
            return DEFAULTS[name]
        else:
            raise AttributeError("'%s' setting not found" % name)


settings = DjangoJabberSettings(_settings)
