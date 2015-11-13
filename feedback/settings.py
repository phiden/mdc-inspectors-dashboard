# -*- coding: utf-8 -*-
import os

os_env = os.environ


class Config(object):
    DEBUG = False
    TESTING = False
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os_env.get('DATABASE_URL')
    BROWSERID_URL = os_env.get('BROWSERID_URL')
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    ADMIN_EMAIL = os_env.get('ADMIN_EMAIL', 'ehsiung@codeforamerica.org')
    CITY_DOMAINS = ['miamidade.gov', 'codeforamerica.org']
    MAIL_USERNAME = os_env.get('MAIL_USERNAME')
    MAIL_PASSWORD = os_env.get('MAIL_PASSWORD')
    MAIL_SERVER = os_env.get('MAIL_SERVER')
    MAIL_DEFAULT_SENDER = os_env.get('MAIL_DEFAULT_SENDER', 'no-reply@miamidade.gov')
    FEEDBACK_SENDER = os_env.get('FEEDBACK_SENDER', 'feedbackbot@miamidade.gov')
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    TF_ID = os_env.get('TF_ID')
    TF_KEY = os_env.get('TF_KEY')
    LANG_EN = os_env.get('LANG_EN')
    ROLE_EN = os_env.get('ROLE_EN')
    ROLE_ES = os_env.get('ROLE_ES')
    OPINION_EN = os_env.get('OPINION_EN')
    OPINION_ES = os_env.get('OPINION_ES')
    GETDONE_EN = os_env.get('GETDONE_EN')
    GETDONE_ES = os_env.get('GETDONE_ES')
    COMMENTS_EN = os_env.get('COMMENTS_EN')
    COMMENTS_ES = os_env.get('COMMENTS_ES')
    TYPE_EN = os_env.get('TYPE_EN')
    TYPE_ES = os_env.get('TYPE_ES')
    FOLLOWUP_EN = os_env.get('FOLLOWUP_EN')
    FOLLOWUP_ES = os_env.get('FOLLOWUP_ES')
    CONTACT_EN = os_env.get('CONTACT_EN')
    CONTACT_ES = os_env.get('CONTACT_ES')


class ProductionConfig(Config):
    ENV = 'prod'
    DEBUG = False
    BROWSERID_URL = os_env.get('BROWSERID_URL', 'http://mdc-feedback.herokuapp.com/')


class StagingConfig(Config):
    ENV = 'stage'
    DEVELOPMENT = True
    DEBUG = True
    MAIL_USERNAME = os_env.get('SENDGRID_USERNAME')
    MAIL_PASSWORD = os_env.get('SENDGRID_PASSWORD')
    MAIL_SERVER = 'smtp.sendgrid.net'
    MAIL_MAX_EMAILS = 100


class DevelopmentConfig(Config):
    ENV = 'dev'
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = os_env.get('DATABASE_URL', 'postgresql://localhost/inspectors_dev')
    DEBUG = True
    DEBUG_TB_ENABLED = True
    ASSETS_DEBUG = True  # Don't bundle/minify static assets
    BROWSERID_URL = os_env.get('BROWSERID_URL', 'http://localhost:9000')
    MAIL_SERVER = 'smtp.gmail.com'  # Use gmail in dev: https://support.google.com/mail/answer/1173270?hl=en
    ADMIN_EMAIL = os_env.get('ADMIN_EMAIL', 'mdcfeedbackdev@gmail.com')
    MAIL_USERNAME = 'mdcfeedbackdev@gmail.com'
    MAIL_PASSWORD = 'miamidade305'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_SUPPRESS_SEND = True


class TestingConfig(Config):
    ADMIN_EMAIL = 'foo@foo.com'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os_env.get('TEST_DATABASE_URL', 'postgresql://localhost/inspectors_test')
    MAIL_SUPPRESS_SEND = True
