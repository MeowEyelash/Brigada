import sentry_sdk
from config.settings import SENTRY_DSN

def setup_sentry():
    if SENTRY_DSN:
        sentry_sdk.init(dsn=SENTRY_DSN)