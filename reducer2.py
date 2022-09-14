#!/usr/bin/env python3
"""reducer.py"""

from operator import itemgetter
from scipy.stats import pearsonr
from requests.exceptions import ConnectionError
import numpy as np

def retry_on_connectionerror(f, max_retries=5):
  retries = 0
  while retries < max_retries:
    try:
      return f()
    except ConnectionError:
      retries += 1
  raise Exception("Maximum retries exceeded")


import sys

current_word = None

list_num_word = []
list_num_answ = []

current_corr = 0
pace = 10

# input comes from STDIN
for i, line in enumerate(sys.stdin):
    # get values
    len_body, answear_count = line.split('\t')

    list_num_word.append(int(len_body))
    list_num_answ.append(int(answear_count[:-1]))

    if i % 10 == 0 and i != 0:
        # get batch of correlation
        corr, _ = pearsonr(list_num_word, list_num_answ)
        
        # skip errors
        if np.isnan(corr):
            continue
            exit()

        corr = float(corr)
        ## skip initial values
        if current_corr == 0:
            current_corr = corr
        ## que the median of the current corrs
        current_corr = (corr + current_corr) / 2
    
        ## erase listts
        list_num_answ = []
        list_num_word = []
    
    print(current_corr)

print(f"final correlation {current_corr}")
