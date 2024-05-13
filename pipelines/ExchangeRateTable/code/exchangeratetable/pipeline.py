from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from exchangeratetable.config.ConfigStore import *
from exchangeratetable.udfs.UDFs import *
from prophecy.utils import *
from exchangeratetable.graph import *

def pipeline(spark: SparkSession) -> None:
    df_L0_raw_exchange_rate_table = L0_raw_exchange_rate_table(spark)
    create_exchange_rate_lookup(spark, df_L0_raw_exchange_rate_table)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("ExchangeRateTable")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/ExchangeRateTable")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/ExchangeRateTable", config = Config)(pipeline)

if __name__ == "__main__":
    main()
