#!/usr/bin/python
# -*- coding: utf-8 -*-

import change
import requests

def RunBatch(data=None):
  '''Runs a batch job for changing frequency.'''

  if data == None:
    print 'No data provided.'
    return False

  i = 1
  total = len(data)
  for record in data:
    print 'Registering record %s / %s' % (i, total)
    print 'ID: %s' % record['ID']
    change.ChangeFrequency(id=record['ID'], frequency=record['Frequency'])
    i += 1
