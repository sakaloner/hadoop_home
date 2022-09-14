#!/usr/bin/env python3
import sys

top_posts = []
count = 0
for line in sys.stdin:
    if 'AnswerCount' not in line:
        continue
    # get the body of the post
    print(f'analizing line {count}')
    items = line.split('"')
    for i, x in enumerate(items):
        if 'AnswerCount' in items[i]:
            try:
                num_answers = int(items[i+1])
            except:
                continue
        if 'Id' in items[i]:
            try:
                id_post = int(items[i+1])
            except:
                continue
    ## analisis
    if len(top_posts) < 10:
        top_posts.append([id_post, num_answers])
    ## sort
    top_posts = sorted(top_posts, key=lambda x: x[1])

    if num_answers > top_posts[0][1]:
        top_posts.pop(0)
        top_posts.append([id_post, num_answers])

print(top_posts)
