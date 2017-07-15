## -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import yaml
import lamvery

try:
    #  with open('config.yml') as f:
    with open(lamvery.secret.file('config.yml')) as f:
        _oauth_conf = yaml.load(f)

except Exception as e:
    print(e)

config = {
        'INCOMING_WEBHOOKS':  _oauth_conf['incoming_webhooks'],
        'BUCKET': _oauth_conf['bucket'],
        'KEY':  _oauth_conf['key'],
        }
