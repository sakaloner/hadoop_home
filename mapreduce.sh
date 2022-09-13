mapred streaming \
-input /hadoop_project/book.txt \  
-output /tmp/guten/analized.txt \
-mapper /home/andresv/hadoop_home/mapper.py \
-reducer /home/andresv/hadoop_home/reducer.py