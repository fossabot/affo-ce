import sys  # noqa

from dynaconf import LazySettings

settings = LazySettings(ENVVAR_PREFIX_FOR_DYNACONF="AFFO_DL", ENVVAR_FOR_DYNACONF="AFFO_DL_SETTINGS")

# DEEPLINK SECRET CONFIGURATION
DEEPLINK_SECRET_KEY = getattr(settings, "DEEPLINK_SECRET_KEY", "")

# EVENTS CONFIGURATION
EVENTS_API_URL = getattr(settings, "EVENTS_API_URL", "http://events.affo.io")

settings.populate_obj(sys.modules[__name__])
