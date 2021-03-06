# -*- coding=utf-8 -*-

import logging
import os

logger = logging.getLogger(__name__)
ENV = os.environ.get

SECRET_KEY = ENV('SECRET_KEY', 'random-secret-key')
SESSION_COOKIE_NAME = ENV('SESSION_COOKIE_NAME', 'vulyk_session')
DEBUG = ENV('DEBUG', True)

MONGODB_SETTINGS = {
    'DB': ENV("mongodb_db", "vulyk"),
    'HOST': ENV("mongodb_host", "localhost"),
    'USERNAME': ENV("mongodb_username", None),
    'PASSWORD': ENV("mongodb_password", None),
    'PORT': (int(ENV("mongodb_port"))
             if ENV("mongodb_port") else None)
}

DEBUG_TB_INTERCEPT_REDIRECTS = ENV('DEBUG_TB_INTERCEPT_REDIRECTS', False)
SESSION_PROTECTION = ENV('SESSION_PROTECTION', 'strong')

SOCIAL_AUTH_STORAGE = ENV('SOCIAL_AUTH_STORAGE',
                          'social.apps.flask_app.me.models.FlaskStorage')
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = ENV('SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL',
                                         True)

SOCIAL_AUTH_LOGIN_URL = ENV('SOCIAL_AUTH_LOGIN_URL', '/')
SOCIAL_AUTH_LOGIN_REDIRECT_URL = ENV('SOCIAL_AUTH_LOGIN_REDIRECT_URL', '/')

SOCIAL_AUTH_USER_MODEL = ENV('SOCIAL_AUTH_USER_MODEL',
                             'vulyk.models.user.User')
SOCIAL_AUTH_AUTHENTICATION_BACKENDS = ENV(
    'SOCIAL_AUTH_AUTHENTICATION_BACKENDS', (
        'social.backends.google.GoogleOAuth2',
        'social.backends.twitter.TwitterOAuth',
        'social.backends.facebook.FacebookOAuth2',
        'social.backends.vk.VKOAuth2',
    ))

# Keypairs for social auth backends
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ENV('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY', '')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ENV('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET', '')

SOCIAL_AUTH_TWITTER_KEY = ENV('SOCIAL_AUTH_TWITTER_KEY', '')
SOCIAL_AUTH_TWITTER_SECRET = ENV('SOCIAL_AUTH_TWITTER_SECRET', '')

SOCIAL_AUTH_FACEBOOK_KEY = ENV('SOCIAL_AUTH_FACEBOOK_KEY', '')
SOCIAL_AUTH_FACEBOOK_SECRET = ENV('SOCIAL_AUTH_FACEBOOK_SECRET', '')

SOCIAL_AUTH_VK_OAUTH2_KEY = ENV('SOCIAL_AUTH_VK_OAUTH2_KEY', '')
SOCIAL_AUTH_VK_APP_SECRET = ENV('SOCIAL_AUTH_VK_APP_SECRET', '')

SOCIAL_AUTH_FACEBOOK_SCOPE = ENV('SOCIAL_AUTH_FACEBOOK_SCOPE', ['email'])

JS_ASSETS = ['vendor/jquery/jquery.js',
             'vendor/jquery.cookie/jquery.cookie.js',
             'vendor/bootstrap/bootstrap.js',
             'vendor/jquery.hotkeys/jquery.hotkeys.js',
             'vendor/jquery.magnific-popup/jquery.magnific-popup.js',
             'scripts/base.js']
JS_ASSETS_OUTPUT = ENV('JS_ASSETS_OUTPUT', 'scripts/packed.js')

JS_ASSETS_FILTERS = ENV('JS_ASSETS_FILTERS', 'yui_js')

CSS_ASSETS = ['vendor/bootstrap/bootstrap.css',
              'vendor/jquery.magnific-popup/jquery.magnific-popup.css',
              'styles/style.css']
CSS_ASSETS_OUTPUT = ENV('CSS_ASSETS_OUTPUT', 'styles/packed.css')
CSS_ASSETS_FILTERS = ENV('CSS_ASSETS_FILTERS', 'yui_css')


# Default redundancy level for processing
USERS_PER_TASK = ENV('USERS_PER_TASK', 2)

# Restrict an access to site to admins only
SITE_IS_CLOSED = ENV('SITE_IS_CLOSED', False)

ENABLED_TASKS = ENV('ENABLED_TASKS', {
    'vulyk.plugins.dummy': 'DummyTaskType',
})

SITE_NAME = 'Vulyk workspace'
SITE_MOTTO = "Vulyk: crowdsourcing platform"

DEFAULT_BATCH='default'

try:
    from werkzeug.utils import import_string

    local_settings = import_string('local_settings')
    for attr in dir(local_settings):
        locals()[attr] = getattr(local_settings, attr)
except Exception as e:
    logger.error(e)
