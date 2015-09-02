#!/usr/bin/python
# -*- coding: utf-8 -*-

import load
import batch

def Main():
  '''Wrapper.'''

  #
  # Change the frequency in batch.
  #
  data = load.LoadCSV()
  batch.RunBatch(data)

if __name__ == '__main__':
  Main()
