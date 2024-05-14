from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from convert_int_to_date.config.ConfigStore import *
from convert_int_to_date.udfs.UDFs import *
from prophecy.utils import *
from convert_int_to_date.graph import *

def pipeline(spark: SparkSession) -> None:
    df_date_dataframe_creation = date_dataframe_creation(spark)
    df_Subgraph_1 = Subgraph_1(spark, Config.Subgraph_1, df_date_dataframe_creation)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("convert_int_to_date")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/convert_int_to_date")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/convert_int_to_date", config = Config)(pipeline)

if __name__ == "__main__":
    main()
