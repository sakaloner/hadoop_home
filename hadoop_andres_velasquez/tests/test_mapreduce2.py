import pytest

from .mapreducers import mapper2, reducer2

def test_mapreduce1():
    path = '/home/andresv/hadoop_home/hadoop_project/112010 Stack Overflow/posts.xml'
    mapreduce1(path)
