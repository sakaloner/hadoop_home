import pytest

from hadoop_andres_velasquez.mapreducers import mapreduce1

def test_mapreduce1():
    path = '/home/andresv/hadoop_home/hadoop_project/112010 Stack Overflow/posts.xml'
    mapreduce1(path)
