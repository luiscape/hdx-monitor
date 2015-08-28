#!/usr/bin/python
# -*- coding: utf-8 -*-

import load
import fetch
import batch

def Main():
  '''Wrapper.'''

  #
  # Downloading latest batch file.
  #
  fetch.DownloadLatestBatchFile()

  #
  # Change the frequency in batch.
  #
  data = load.LoadCSV()
  batch.RunBatch(data)

if __name__ == '__main__':
  Main()
