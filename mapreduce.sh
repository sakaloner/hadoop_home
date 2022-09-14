mapred streaming \
    -input '/home/andresv/hadoop_home/hadoop_project/112010 Stack Overflow/posts.xml' \  
    -output /home/andresv/hadoop_home/analized.txt \
    -mapper /home/andresv/hadoop_home/mapper2.py \
    -reducer /home/andresv/hadoop_home/reducer2.py


mapred streaming -input '/home/andresv/hadoop_home/hadoop_project/112010 Stack Overflow/posts.xml' -output /home/andresv/hadoop_home/analized.txt -mapper /home/andresv/hadoop_home/mapper2.py -reducer /home/andresv/hadoop_home/reducer2.py