#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv

def LoadCSV(path='data/batch.csv'):
  '''Load CSV file.'''

  out = []
  with open(path, 'r') as f:
    data = csv.DictReader(f)
    for row in data:
      out.append(row)

    return out
