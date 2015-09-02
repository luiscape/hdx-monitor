#!/usr/bin/python
# -*- coding: utf-8 -*-

import age

def RunBatch(data=None):
  '''Runs a batch job for changing frequency.'''

  if data == None:
    print 'No data provided.'
    return False

  i = 1
  total = len(data)
  for record in data:
    print 'Calculating age of %s / %s' % (i, total)
    print 'ID: %s' % record['ID']
    age.CalculateAge(id=record['ID'])
    i += 1
