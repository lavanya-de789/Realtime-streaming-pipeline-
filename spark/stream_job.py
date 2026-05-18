from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark=(SparkSession.builder
.appName('StockStreaming')
.getOrCreate())

schema=StructType([
StructField('symbol',StringType()),
StructField('price',DoubleType()),
StructField('timestamp',StringType())
])

raw=(spark.readStream
.format('kafka')
.option(
'kafka.bootstrap.servers',
'localhost:9092')
.option('subscribe',
'stock-topic')
.load())

parsed=(raw.select(
from_json(
col('value').cast('string'),
schema
).alias('data')
).select('data.*'))

query=(parsed.writeStream
.format('parquet')
.option(
'path',
'data/bronze')
.option(
'checkpointLocation',
'data/checkpoint')
.outputMode('append')
.start())

query.awaitTermination()
