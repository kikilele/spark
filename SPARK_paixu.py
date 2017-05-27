from pyspark import SparkContext
from pyspark import SparkFiles

sc = SparkContext(appName="paixu")
tmp = sc.textFile('A.txt')
tmp1 = tmp.map(lambda x:x.split())
tmp2 = tmp1.sortBy(lambda x: (x[0],x[1]))

print tmp2.collect()







