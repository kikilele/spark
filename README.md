ʵ�ֶ�һ���ļ��Ķ������ݽ��кϲ��������ж�������
�����ļ��е�ÿ�����ݾ�Ϊ������������Ҫ���Ȱ��յ�һ��������С���������һ����ͬ�����յڶ���������С�����Դ����ơ�


���磬�����ļ����£�
A.txt:
20	21 
10 	51 
30 	22 
20 	53 
30 	44 
60 	43 
60 	11 

�����
B.txt:
10	51
20	21
20	53
30	22
30	44
60	11
60	43



Hadoop��
ִ�����
bin/hadoop jar contrib/streaming/hadoop-streaming-1.2.1.jar -D mapred.reduce.tasks=1 -mapper mapper.py -file mapper.py -reducer reducer.py -file reducer.py -input hdfs://master:9000/user/centos/a.txt -output hdfs://master:9000/centos/output5
Ҳ����ִ�м򵥵Ĳ��ԣ�
cat a.txt | map.py | sort | redu.py


