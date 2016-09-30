# from coursework.settings import *
# import logging
#
# try:
#     from coursework.settings import LOGGING
# except ImportError:
#     LOGGING = dict(version=1, disable_existing_loggers=False, handlers={}, loggers={})
#
# DATABASES = {
#     'default': {
#         'ENGINE'      : 'django.db.backends.sqlite3',
#         'NAME'        : ':memory:',
#         'USER'        : '',
#         'PASSWORD'    : '',
#         'TEST_CHARSET': 'utf8',
#     }}
#
# LOGGING['handlers']['console'] = {
#     'level': 'DEBUG',
#     'class': 'logging.StreamHandler',
# }
#
# LOGGING['loggers']['django.db.backends'] = {
#     'handlers' : ['console'],
#     'level'    : 'DEBUG',
#     'propagate': False,
# }
#
# LOGGING['loggers']['django.db.backends.schema'] = {
#     'propagate': False,  # don't log schema queries, django >= 1.7
# }
