#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests


def ChangeFrequency(id=None, frequency=None):
  '''Changes the frequency of a dataset in HDX.'''

  if id == None or frequency == None:
    print 'No id or frequency provided.'
    return False

  #
  # TODO: API hard-coded.
  #
  h = {
    'X-CKAN-API-Key' : 'a6863277-f35e-4f50-af85-78a2d9ebcdd3',
    'Content-Type' : 'application/json'
    }
  d = { 'id' : id, 'data_update_frequency' : frequency }
  url = 'https://data.hdx.rwlabs.org/api/action/hdx_package_update_metadata'

  #
  # Making request.
  #
  r = requests.post(url, headers=h, data=json.dumps(d))

  if r.status_code == 200:
    print r.json()['success']

  else:
    print r.json()['success']
