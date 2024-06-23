from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("calcul_avocado_volume").getOrCreate()
df = spark.read.csv("hdfs:///raw_avocado/avocado_1.csv", header=True, inferSchema=True)
sum_volume = df.groupBy().sum("Volume").collect()[0][0]
spark.sql(f"INSERT INTO TP_MASTER.avocado_volume_tracking VALUES ('avocado_1.csv', {sum_volume})")
df.write.csv("hdfs:///stagging_avocado/avocado_1.csv", mode="overwrite", header=True)
spark.stop()









