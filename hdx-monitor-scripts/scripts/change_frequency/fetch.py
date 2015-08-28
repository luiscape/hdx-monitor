#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import requests

def DownloadLatestBatchFile(path='data/batch.csv'):
  '''Downlods a CSV batch file from Google Docs and stores locally.'''

  dir = os.path.join(os.getcwd(), path)
  url = 'https://docs.google.com/spreadsheets/d/1e-KTh2Q9r9BMtkKiWB7tyMCulZL0aXGJvXO1wVTppuM/pub?gid=56769263&single=true&output=csv'
  r = requests.get(url)
  with open(dir, 'wb') as f:
    for chunk in r.iter_content():
      f.write(chunk)
