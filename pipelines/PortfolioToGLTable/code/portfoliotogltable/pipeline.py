from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from portfoliotogltable.config.ConfigStore import *
from portfoliotogltable.udfs.UDFs import *
from prophecy.utils import *
from portfoliotogltable.graph import *

def pipeline(spark: SparkSession) -> None:
    df_L0_Portfolio_to_GL = L0_Portfolio_to_GL(spark)
    create_portfolio_to_gl_lookup(spark, df_L0_Portfolio_to_GL)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("PortfolioToGLTable")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/PortfolioToGLTable")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/PortfolioToGLTable", config = Config)(pipeline)

if __name__ == "__main__":
    main()
