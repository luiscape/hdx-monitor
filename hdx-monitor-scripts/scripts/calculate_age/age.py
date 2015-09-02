#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests


def CalculateAge(id=None):
  '''Changes the frequency of a dataset in HDX.'''

  if id == None:
    print 'No id provided.'
    return False

  #
  # TODO: API hard-coded.
  #
  url = 'http://192.168.99.100:3000/v1/update/' + id + '/'

  #
  # Making request.
  #
  r = requests.get(url)

  if r.status_code == 200:
    print r.json()

  else:
    print r.json()
