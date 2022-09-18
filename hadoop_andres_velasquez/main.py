from mapreducers import mapreduce1
from mapreducers import mapper2, mapper3
from mapreducers import reducer2, reducer3

def main():
    ''' Main function to run all the mapreduce functions'''
    path = '/home/andresv/hadoop_home/hadoop_project/112010 Stack Overflow/posts.xml'
    mapreduce1(path)
    mapper2(path)
    reducer2(path)
    mapper3(path)
    reducer3(path)

if __name__ == "__main__":
    main()

