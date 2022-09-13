#!/usr/bin/env python3
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # ignore irrelevant xml tags
    if 'Body' not in line:
        continue
    # get the body of the post
    items = line.split('"')
    for i, x in enumerate(items):
        if 'Body' in items[i]:
            body = items[i+1]
            len_body = len(body)
        if 'AnswerCount' in items[i]:
            answear_count = items[i+1]
    
    print(f'{len_body}\t{answear_count}')
    
    
    # get the words in the body
    # for body in bodies:
    #     words = body.split()
    #     for word in words:
            # write the results to STDOUT (standard output);
            # what we output here will be the input for the
            # Reduce step, i.e. the input for reducer.py
            #
            # tab-delimited; the trivial word count is 1
            # print ('%s\t%s' % (word, 1))
    
            
    # for item in items:
    #     if 'Body' in item:
    #         print (f'{item}\t1')


    # # remove leading and trailing whitespace
    # line = line.strip()
    # # split the line into words
    # words = line.split()
    # # increase counters
    # for word in words:
    #     # write the results to STDOUT (standard output);
    #     # what we output here will be the input for the
    #     # Reduce step, i.e. the input for reducer.py
    #     #
    #     # tab-delimited; the trivial word count is 1
    #     print (f'{word}\t {1}')

