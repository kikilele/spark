实现对一个文件的多列数据进行合并，并进行二次排序
输入文件中的每行内容均为两个个整数。要求先按照第一列整数大小排序，如果第一列相同，按照第二列整数大小排序，以此类推。


例如，输入文件如下：
A.txt:
20	21 
10 	51 
30 	22 
20 	53 
30 	44 
60 	43 
60 	11 

输出：
B.txt:
10	51
20	21
20	53
30	22
30	44
60	11
60	43



Hadoop：
执行命令：
bin/hadoop jar contrib/streaming/hadoop-streaming-1.2.1.jar -D mapred.reduce.tasks=1 -mapper mapper.py -file mapper.py -reducer reducer.py -file reducer.py -input hdfs://master:9000/user/centos/a.txt -output hdfs://master:9000/centos/output5
也可以执行简单的测试：
cat a.txt | map.py | sort | redu.py


