# Import the PySpark module
from pyspark.sql import SparkSession

# Create SparkSession object
spark = SparkSession.builder \
                    .master('local[*]') \
                    .appName('test') \
                    .getOrCreate()


# What version of Spark?
print(spark.version)

# Terminate the cluster
# spark.stop()